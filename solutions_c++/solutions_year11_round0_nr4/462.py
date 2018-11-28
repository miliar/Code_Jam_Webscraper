#include <iostream> 
#include <fstream>
using namespace std; 

//double expt(int n);
//double expt(int n)
//{
//    double ans;
//    if (n==2)
//    return 2;
//    else
//    ans = expt(n-1)/(n+1)*n+1;
//    return ans;
//}

int main() { 
 int n[1000];
 int N;
 int tests;
 int sorted[1000];
 ifstream input("D-large.in");
 ofstream output("D-large.out");
 input >> tests;
 
 for (int j=0;j<tests;j++)
 {
     input >> N;
     double total=0;
     for (int i=0;i<N;i++)
     {
         input >> n[i];
         sorted[i]=0;
     }
     for (int i=0;i<N;i++)
     {
         if (n[i]==i+1)
            sorted[i]=1;
         if (sorted[i]==1)
            continue;
         int count=1;
         int now=n[i];
         sorted[i]=1;
         while (n[now-1]!=n[i])
         {
            sorted[now-1]=1;
            count++;
            now=n[now-1];
         }
         total+=count;
     }

     
     
     output << "Case #" << (j+1) << ": " << total << "\n";
 }


 return 0; 
}
