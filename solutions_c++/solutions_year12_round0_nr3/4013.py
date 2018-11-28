#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <string>
#include <map>

using namespace std;
string makestring(long int n){
     ostringstream oss1;
     oss1 << n; 
     return  oss1.str(); 
}
bool checkChars(long int m, long int n){
     map<char, int> charsm, charsn;
     ostringstream oss1, oss2;
     oss1 << m; oss2 << n;
     string sm = oss1.str(); string sn = oss2.str();

     for (int i = 0; i< sm.length(); i++){
         char c = sm[i]; char c2= sn[i];
         charsm[c]++; charsn[c2]++;
     }
     
     string nums = "0123456789";
     for (int j = 0 ; j< 10; j++){
         char c = nums[j]; if (charsm[c] != charsn[c]) return false;
     }      
     return true;         
}
void check(long int n, long int m){
     //cout << "checking " << n << " & " << m << endl;
     string sn = makestring(n);
     string sm = makestring(m);
     
     
     }
int solveCase(long int A, long int B){
    long int newint, count=0;
    string number, newnumber;
    bool nodup;
    pair<map<int,int>::iterator,bool> ret;
    
    for (int i = A; i<=B; i++){
        number = makestring(i);
        map<int,int> datain;
        for (int j = 1; j < number.length(); j++){
            newnumber = number.substr(j,number.length()-j) + number.substr(0,j) ;
            newint = atoi(newnumber.c_str());

            nodup = true;
            ret = datain.insert (pair<int,int>(newint,1));             
            
            if (ret.second==false)
                        nodup = false;

            if ( (newint >= A) && (newint <=B) && (newint > i) && (nodup) )
               count++;              
        }
    }
    return count;
}

int main()
{
	int T,A,B;

	cin >> T;
	for (int i=0;i<T;i++)
	{
        cin >> A;
        cin >> B;

	   cout << "Case #" << i+1 << ": " << solveCase(A,B) <<endl;
	}
	return 0;
}
