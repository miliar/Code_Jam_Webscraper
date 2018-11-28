#include <iostream>

using namespace std;

int pre1[11][31];
int pre2[11][31];

int main()
{
    for(int i=0; i<=10; i++)
    {
            for(int j=0; j<=10; j++)
            {
                    for(int k=0; k<=10; k++)
                    {
                            if(abs(i-j)<2 && abs(i-k)<2 && abs(j-k)<2)
                            {
                                          int m=max(i,max(j,k));
                                          pre1[m][i+j+k]=1;
                            }
                    }
            }
    }
    for(int i=0; i<=10; i++)
    {
            for(int j=0; j<=10; j++)
            {
                    for(int k=0; k<=10; k++)
                    {
                            if(abs(i-j)<=2 && abs(i-k)<=2 && abs(j-k)<=2)
                            {
                                           if(abs(i-j)==2 || abs(j-k)==2 || abs(i-k)==2)
                                           {
                                                          int m=max(i,max(j,k));
                                                          pre2[m][i+j+k]=1;
                                           }
                            }
                    }
            }
    }
    
    int t;
    cin >> t;
    int n,s,p;
    for(int i=0; i<t; i++)
    {
            cin >> n >> s >> p;
            int a[n];
            int val[n];
            int sur[n];
            for(int j=0; j<n; j++)
            {
                    cin >> a[j];
                    val[j]=0;
                    sur[j]=0;
            }
            
            int ans=0;
            for(int j=0; j<n; j++)
            {
                    for(int k=p; k<=10; k++)
                    {
                            if(pre1[k][a[j]]==1)
                            {
                                                val[j]=1;
                            }
                            if(pre2[k][a[j]]==1)
                            {
                                                sur[j]=1;
                            }
                    }
            }
            for(int j=0; j<n; j++)
            {
                    if(val[j]==1)
                    {
                                 ans++;
                    }
                    else if(sur[j]==1)
                    {
                         if(s>0)
                         {
                                ans++;
                                s--;
                         }
                    }
            }
            cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
