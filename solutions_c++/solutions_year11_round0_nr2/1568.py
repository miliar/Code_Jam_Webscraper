#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;

int C,D,N;
char comb[40][3],opp[30][2],des[200];

int combine(char a,char b)
{
    int i;
    for(i=0;i<C;i++)
    {
        if(comb[i][0]==a && comb[i][1]==b)
           return i;
        if(comb[i][1]==a && comb[i][0]==b)
           return i;
    }
    return -1;
}

bool clear(char *a,int len)
{
     int i,j;
     for(i=0;i<D;i++)
     {
         if(a[len-1]==opp[i][0])
         {
             for(j=0;j<len-1;j++)
                if(opp[i][1]==a[j])
                {
              //    cout << j << ": " << opp[i][0] << opp[i][1]<<endl;
                  return true;
                }
         }
         if(a[len-1]==opp[i][1])
         {
              for(j=0;j<len-1;j++)
                if(opp[i][0]==a[j])
                {
              //    cout << j << ": " << opp[i][0] << opp[i][1]<<endl;
                  return true;
                }
         }
     }
     return false;
}
int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\B-large.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Downloads\\out", "w", stdout);
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++)
    {
        
        cin>>C;
      //  cout<<C;
        int j;
        for(j=0;j<C;j++)
        {
            cin>>comb[j][0]>>comb[j][1]>>comb[j][2];
      //      cout<<comb[j][0]<<comb[j][1]<<comb[j][2];
        }
        cin>>D;
       // cout<<D;
        for(j=0;j<D;j++)
        {
            cin>>opp[j][0]>>opp[j][1];
      //     cout<<opp[j][0]<<opp[j][1];
        }
        cin>>N;
       // cout<<N;
        for(j=0;j<N;j++)
        {
            cin>>des[j];
          //  cout<<des[j];
        }
        char ans[200],len=0;
        for(j=0;j<N;j++)
        {
            ans[len++] = des[j];
            int tmp;
            if( (tmp=combine(ans[len-2],ans[len-1])) != -1 )
            {
                ans[len-2] = comb[tmp][2];
                len--;
                continue;
            }
            if( clear(ans,len) )
                len = 0;
        }
        cout << "Case #" << i+1 << ": [";
        if( len > 0 )
           cout << ans[0];
        for(j=1;j<len;j++)
           cout << ", " << ans[j];
        cout << "]" << endl;
    }
 //   system("pause");
    return 0;
}
