#include <iostream>
#include <vector>
using namespace std;

char water(int i,int j,char &ch,int a[][128],char f[][128])
{
    if(!(f[i][j]>='a' && f[i][j]<='z'))
    {
        if(a[i-1][j]<=a[i+1][j] && a[i-1][j]<=a[i][j-1] && a[i-1][j]<=a[i][j+1] && a[i-1][j]<a[i][j])
            return f[i][j]=water(i-1,j,ch,a,f);
        else if(a[i][j-1]<=a[i-1][j] && a[i][j-1]<=a[i+1][j] && a[i][j-1]<=a[i][j+1] && a[i][j-1]<a[i][j])
            return f[i][j]=water(i,j-1,ch,a,f);
        else if(a[i][j+1]<=a[i-1][j] && a[i][j+1]<=a[i][j-1] && a[i][j+1]<=a[i+1][j] && a[i][j+1]<a[i][j])
            return f[i][j]=water(i,j+1,ch,a,f);
        else if(a[i+1][j]<=a[i-1][j] && a[i+1][j]<=a[i][j-1] && a[i+1][j]<=a[i][j+1] && a[i+1][j]<a[i][j])
            return f[i][j]=water(i+1,j,ch,a,f);
        else if(a[i][j]<=a[i-1][j] && a[i][j]<=a[i][j-1] && a[i][j]<=a[i][j+1] && a[i][j]<=a[i+1][j])
            return f[i][j]=ch++;
    }
    else
        return f[i][j];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int N;
    cin >> N;
    for(int i=1;i<=N;++i)
    {
        int H,W;
        cin >> H >> W;
        char f[128][128]={0};
        int a[128][128];
        memset(a,127,sizeof(a));
        for(int j=1;j<=H;++j)
            for(int k=1;k<=W;++k)
                cin >> a[j][k];
        char ch='a';
        for(int j=1;j<=H;++j)
            for(int k=1;k<=W;++k)
                f[j][k]=water(j,k,ch,a,f);
        cout << "Case #" << i << ":" << endl;
        for(int j=1;j<=H;++j)
        {
            for(int k=1;k<=W;++k)
                cout << f[j][k] << ' ';
            cout << endl;
        }
    }
	return 0;
}