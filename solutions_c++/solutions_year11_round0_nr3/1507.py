#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int n_case;
int res=0;
int total=0;
int main()
{
    ofstream  cout("out.txt");
   freopen("in.txt","r",stdin);
    int n;
    cin>>n_case;
    for(int t=0;t<n_case;t++){
    cin>>n;
    int tmp;
    res=0;
    total=0;
    int min_tmp=99999999;
    for(int i=0;i<n;i++)
      {
          cin>>tmp;
          total+=tmp;
          if(tmp<min_tmp)
          min_tmp=tmp;
          res=res^tmp;
      }
    if(res!=0)
    cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
    else  cout<<"Case #"<<t+1<<": "<<total-min_tmp<<endl;
    }
}



