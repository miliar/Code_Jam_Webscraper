
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <deque>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <set>
#include <map>
#include <numeric>
#include <ctime>
#include <functional>
#include <queue>

using namespace std;

int main()
{
    FILE *f,*fw;
    int t,n1,n2;
    char c;
    int i=0,j,k,m,temp,temp2,temp3,digits=0,cur,ans=0,temp4,temp5;;
    string s;
    vector<int> ans_vec;
    f=fopen("C-large.in","r");
    fw=fopen("ans_2.txt","w");
    fscanf(f,"%d",&t);
    //while (i>=0)
    //{
    //      if (i%100000==0)cout<<i<<" ";i+=100000;}
    //system("pause");
    //cout<<t;
    //system("pause");
    for (i=0;i<t;i++)
    {
        fscanf(f,"%d%d",&n1,&n2);
        //cout<<n1<<" "<<n2<<endl;
        temp=n2;
        digits=0;
        //cout<<"hg ";
        ans=0;
        while(temp)
        {digits++;temp/=10;
        }
        //cout<<digits<<endl;
        for (j=n1;j<n2;j++)
        {
            ans_vec.clear();
            for (k=1;k<digits;k++)
            {
                temp=j;
                cur=(int)(pow(10.0,(double)k)+.5);
                //cout<<"varun "<<cur;
                //system("pause");
                temp2=j%cur;
                temp=j/cur;
                temp4=(int)(pow(10.0,(double)(digits-k))+.5);
                temp5=temp2*temp4;
                temp3=temp+temp5;
                if (temp3>j && temp3<=n2)
                {
                   for (m=0;m<ans_vec.size();m++)
                   {
                       if (temp3==ans_vec[m])
                          break;
                   }
                   if (m==ans_vec.size())
                   {
                      ans++;
                      //cout<<j<<" "<<temp3<<" "<<temp<<" "<<temp2<<" "<<temp4<<" "<<temp5<<cur<<endl;
                      ans_vec.push_back(temp3);
                   }
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
        fprintf(fw,"Case #%d: %d\n",i+1,ans); 
        //system("pause");
    }
        
    fclose(fw);    
    fclose(f);
    system("pause");
    return 0;
}
