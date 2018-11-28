#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;


int ele[100];

/*int gcd(int a, int b)
{
    if (b==1) {return 1;}
    else if (a%b==0) {return b;}
    else {
         return gcd(b,a%b); }
}

int lcd(int a ,int b)
{
    if (a<b) { int temp = b; b=a; a=temp; }
    int g = gcd (a,b);
    return ((a/g)*(b));
}
*/

int main(){
    ifstream fin;
    ofstream fout;
    
    fin.open("a.in");
    fout.open("output.txt");
    int test=0;
    int t;
    fin>>t;
    while (test!=t)
    {
          test++;
          int n;
          int low;
          int high;
          fin>>n>>low>>high;
          memset(ele,0,sizeof(ele));
          for (int i=0; i< n; i++)
          {
              fin>>ele[i];
          }
          //sort(ele[0],ele[n-1]);
          //int at_least = lcd (ele[0], ele[1]);
          int ans = -1;
          /*for (int i=2; i<n; i ++)
          {
              at_least = lcd (at_least, ele[i]);
          }*/
          for (int i=low; i<=high; i++)
          {
              bool okay = true;
              for (int j = 0; ((j<n)&&(okay)); j++){
              if ((i%ele[j]==0)||(ele[j]%i==0)) {;}
              else {okay = false;}}
              if (okay) {ans= i; break;}
          }
          
          fout<<"Case #"<<test<<": ";//something to add
          cout<<"Case #"<<test<<": ";//something to add
          if (ans!=-1)
          { fout<<ans<<endl; cout<<ans<<endl; }
          else {fout<<"NO\n"; cout<<"NO\n";}
          
    }
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}
