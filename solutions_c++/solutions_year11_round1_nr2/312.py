#include <iostream>
#include <string>
using namespace std;
int tn,t;
int n,m;
string dict[10001];
string list[101],ans[101];
bool map[10010][30];
bool v[10010];
bool guess[11];

void init_map(int x,int y)
{
     memset(map,0,sizeof map);     
     int i,j;
     char ch;
     for (i=1;i<=n;i++)
         for (ch='a';ch<='z';ch++)
         {
             if (dict[y].length()!=dict[i].length())
                map[i][ch-'a']=1;
             else
             {
                 for (j=0;j<dict[y].length();j++)
                     if ((dict[y][j]==ch)^(dict[i][j]==ch))
                     {
                         map[i][ch-'a']=1;
                         break;
                     }
             }
         }
}

bool proper(int x,char ch)
{
     int loc=0;
     bool flag=false;
    while((loc=(dict[x].find(ch,loc)))!=string::npos)   
    {
        if (guess[loc])
           return false;
        loc++;
        flag=true;
    }     
    return flag;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    
    int i,j,k,l;
    cin >> tn;
    for (t=1;t<=tn;t++)
    {
        cin >> n >> m;
        cin.get();
        for (i=1;i<=n;i++)
            getline(cin,dict[i]);
        for (i=1;i<=m;i++)
            getline(cin,list[i]);
        
        for (i=1;i<=m;i++)
        {
            int mm=-1,mid=-1;
            for (j=1;j<=n;j++)
            {
                memset(v,0,sizeof v);
                init_map(i,j);
                int sum=0;     
                int len=dict[j].length();  
                memset(guess,0,sizeof guess);     
                for (l=1;l<=n;l++)
                    if (dict[j].length()!=dict[l].length())
                       v[l]=true;    
                //v[j]=true;
                                
                for (k=0;k<=list[i].length();k++)
                {
                    bool flag=false;                   
                    for (l=1;l<=n;l++)
                    {
                        if (!v[l] && proper(l,list[i][k])) //Guess
                        {
                            flag=true;
                            break;
                        }
                    }
                    if (flag)
                    {
                           if (dict[j].find(list[i][k])==string::npos)
                              sum++;
                           for (l=1;l<=n;l++)
                               if (!v[l] && map[l][list[i][k]-'a'])
                                  v[l]=true;
                           int loc=0,count=0;
                           while((loc=(dict[j].find(list[i][k],loc)))!=string::npos)   
                           {
                                guess[loc]=true;
                                loc++;
                                count++;   
                           }
                           len-=count;
                           if (len<=0)
                              break;                             
                    }
                    
                }
                if (sum>mm)
                {
                   mm=sum;
                   mid=j;
                }
            }
            ans[i]=dict[mid];
        }
        
        cout << "Case #" << t << ":";
        for (i=1;i<=m;i++)
            cout << ' ' << ans[i];
        cout << endl;
    }
}
