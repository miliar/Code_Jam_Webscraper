#include <iostream>
#include <fstream>
bool check(int, int);
using namespace std;
int main(char **argv,int argc)
{
   int lineNum;
   cin >> lineNum;
   for (int i=0;i<lineNum;++i)
   {
       long n,num;
	   cin >> n >> num;
	   bool rlt=check(n,num);
	   if (rlt) cout << "Case #" << i+1 << ": ON" << endl;
	   else  cout << "Case #" << i+1 << ": OFF" << endl;
   }
   return 0;
}
bool check(int n,int num)
{
   do{
     if (num==0) return false;
	 if (num&1) --n;
	 else return false;
	 num=num>>1;
//     cout << num << endl;
   }while(n>0&&num>0);
   if (n!=0) return false;
   return true;
}
