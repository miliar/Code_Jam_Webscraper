#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#include<stdio.h>
#include<string.h>

using namespace std;

vector < vector<long long int> > allSubsets (vector<long long int> A, int n){
/*
   Find all possible subsets which will be a 2-D vector
   i.e. vector of vectors.
*/

   // If we have reached beyond the last element
   // just return empty vector indicating empty subset.
   if ( n == A.size() ){
      vector < vector <long long int> > res(1);
      return res;
   }

   // Else, find solution for remaining portion of set
   // after the current element.
   vector <vector <long long int> > result = allSubsets(A, n+1);
   int rn = result.size();

   // Now, add current element to every set in this result
   // and add these new sets to the result.
   for ( int i=0; i< rn; i++ ){
      vector <long long int> temp = result[i];
      temp.push_back( A[n] );
      result.push_back( temp );
   }

   return result;
}

bool disjoint ( vector<long long int> A, vector<long long int> B ){
/*
   Check if sets A and B have any common element.
   Returns True if they don't, False otherwise.
*/
   for ( int i=0; i<A.size(); i++)
      for ( int j=0; j<B.size(); j++)
         if ( A[i] == B[j] )
            return false;

   return true;
}

long long int sum (vector <long long int> A){
/*
   Returns sum of the elements in A
*/
   long long int s=0;
   for (int i=0; i<A.size(); i++)
      s += A[i];

   return s;
}


main()
{
     vector < vector <long long int> > all;
    ifstream ifs;
    ofstream ofs;
    ifs.open("input.txt");
    ofs.open("output.txt");
    int t;
    ifs>>t;
    for(int z=0;z<t;z++)
    {
        int n;
   ifs >> n ;
   vector<long long int> A(n);

   for (int i=0; i<n; i++){
      ifs >> A[i];
   }

   // Find all possible subsets in A
   all = allSubsets(A, 0);

   // Remove the empty subset
   all.erase(all.begin());

   int m = 0;
   bool flag = false;
   // Try all nC2 combinations of subsets to find
   // if any have same sum.
   for ( int i=0; i < all.size()-1; i++){
      for ( int j=i+1; j< all.size(); j++){
         if ( sum( all[i] ) == sum( all[j] ) &&
              disjoint( all[i], all[j] ) ) // Also make sure they have no common elements
         {
             ofs<<"Case #"<<(z+1)<<": "<<endl;
            for(int l=0;l<all[i].size();l++)
              ofs<<all[i][l]<<" ";
             ofs<<endl;
             for(int m = 0;m<all[j].size();m++)
              ofs<<all[j][m]<<" ";
             ofs<<endl;
             flag = true;
         }
         if (flag == true)
          break;
      }
      if(flag == true)
       break;
   }

   if ( flag == false )         // Found some partition
      ofs << "Impossible" << endl;


    }
    ifs.close();
    ofs.close();
}

