#include <iostream>
#include <cmath>
using namespace std;

int tn;
int n,s,p;
int score[200];

void sort()
{
     int i,j;
     for (i=0;i<n-1;i++)
         for (j=i+1;j<n;j++)
             if (score[i]<score[j])
             {
                 int tmp = score[i];
                 score[i] = score[j];
                 score[j] = tmp;
             }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);    
     
    int i,j;
    cin >> tn;
    for (int t=1;t<=tn;t++)
    {
        cin >> n >> s >> p;
        for (i=0;i<n;i++)
            cin >> score[i];
        sort();
        
        int ans = 0;
        for (i=0;i<n;i++)
            if ((score[i]+2)/3 >= p)
               ans++;
            else
                break;
        if (i<n)
            for (j=1;j<=s;j++)
                if ((score[i]>=2 && (score[i]-2)/3+2 >= p) || (score[i]<2 && score[i] >= p))
                {
                   ans++;
                   i++;
                }
                else
                    break;
        
        cout << "Case #" << t << ": " << ans << endl;
    }
}
