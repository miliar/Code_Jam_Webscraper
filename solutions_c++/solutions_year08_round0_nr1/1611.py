#include <iostream>
#include <string>
using namespace std;
struct data
{
      bool* mark;
      string*  s;
      int S;
      int x;
      data(int n){
             x=0;
             S=n;
             mark=new bool[n];
             for(int i=0;i<n;++i)
             {
                     mark[i]=false;
             }
             s=new string[n]();
      }
      ~data(){
              delete[] mark;
              delete[] s;
      }
      bool checkandmark(string in){
           for(int i=0;i<S;++i)
           {
                   if(s[i]==in)
                   {
                               if(mark[i]==false)++x;
                               mark[i]=true;
                               if(x==S)
                               {
                                        reset(i);
                                        return true;
                               }
                   }
           }
           return false;
      }    
      void reset(int p){
              x=1;
              for(int i=0;i<S;++i){
                      mark[i]=false;
              }
              mark[p]=true;
              return;
      }
};
int change(string in){
    int result=0;
    for(int i=0;i<in.length();++i)
    {
                 result*=10;
                 result+=in[i]-'0';   
    }
    return result;
}
int main()
{
    int N,S,Q;
    string num;
    getline(cin,num);
    N=change(num);
    for(int i=0;i<N;++i){
            getline(cin,num);
            S=change(num);
            data a(S);
            for(int j=0;j<S;++j)
            {
                    getline(cin,a.s[j]);
            }
            getline(cin,num);
            Q=change(num);
            
            string temp;
            int result=0;
            for(int k=0;k<Q;++k)
            {
                    getline(cin,temp);
                    result+=a.checkandmark(temp);
            }
            cout<<"Case #"<<i+1<<": "<<result<<endl;
    }
    return 0;
}
