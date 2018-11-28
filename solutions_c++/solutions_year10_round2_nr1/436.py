#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout
#define F(i,n) for((i)=0;(i)<(n);(i)++)

void repeat()
{
     int N,M;
     int i,j,k;
     string temp;
     char *f;
     int c=0;
     map <string,int> dir;
     cin>>N>>M;
     F(i,N) {
            string x="";
            cin>>temp;
            k=temp.size();
            //f=(char*)temp+1;
            for(j=1;j<k;j++)
            {
                           if(temp[j]=='/')
                           {
                                           if(!dir[x])
                                                      dir[x]=1;
                           }
                           x+=temp[j];
            }
            if(!dir[x])
            {
                       dir[x]=1;
            }
     }
     F(i,M) {
            string x="";
            cin>>temp;
            k=temp.size();
            for(j=1;j<k;j++)
            {
                          if(temp[j]=='/')
                          {
                                          if(!dir[x])
                                          {
                                                     c++;
                                                     dir[x]=1;
                                          }
                          }
                          x+=temp[j];
            }
            if(!dir[x])
            {
                       dir[x]=1;
                       c++;
            }
     }
     
     gout<<c<<endl;
}

int main(int argc, char *argv[])
{
    int i,T;
    case_number = 0;
    cin>>T;
    F(i,T)
          repeat();
}
