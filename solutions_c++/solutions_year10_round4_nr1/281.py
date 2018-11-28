#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int T,K;
int num[110][110];

bool check_hor(int n)
{
    int i,j;
    //cout<<"hor.."<<n<<endl;
    int cen=K+n-1;
    int size=K-abs(n);
    for(i=cen-size+1;i<cen;++i)
    for(j=K-size+cen-i;j<=K-2+size-cen+i;j+=2)
    {
        //cout<<num[i][j]<<" "<<num[cen+cen-i][j]<<endl;
        if(num[i][j]!=num[cen+cen-i][j])
            return 0;
    }
    return 1;
};

bool check_ver(int n)
{
    int i,j;
    //cout<<"ver.."<<n<<endl;
    int cen=K+n-1;
    int size=K-abs(n);
    for(i=cen-size+1;i<cen;++i)
    for(j=K-size+cen-i;j<=K-2+size-cen+i;j+=2)
    {
        //cout<<num[j][i]<<" "<<num[j][cen+cen-i]<<endl;
        
        if(num[j][i]!=num[j][cen+cen-i])
            return 0;
    }
    return 1;
};

int main()
{
    int i,j,k;
    ifstream fin("A-large.in");
    FILE* fp=fopen("A_large.txt","w+");
    
    int hor,ver;
    fin>>T;
    for(i=0;i<T;++i)
    {
        for(j=0;j<110;++j)
            memset(num[j],0,sizeof(int)*110);
        
        fin>>K;
        for(j=0;j<K;++j)
        for(k=0;k<j+1;++k)
            fin>>num[j][K-j-1+2*k];
        for(j=K-2;j>=0;--j)
        for(k=0;k<j+1;++k)
            fin>>num[2*K-2-j][K-1-j+2*k];
        /*
        for(j=0;j<2*K-1;++j)
        {
            for(k=0;k<2*K-1;++k)
                cout<<num[j][k];
            cout<<endl;
        }
        system("pause");
        */
        hor=0;
        while(1)
        {
            if(check_hor(hor))
                break;
            if(check_hor(0-hor))
                break;
            ++hor;
        }
        ver=0;
        while(1)
        {
            if(check_ver(ver))
                break;
            if(check_ver(0-ver))
                break;
            ++ver;
        }
        cout<<hor<<" "<<ver<<endl;
        //system("pause");
        fprintf(fp,"Case #%d: %d\n",i+1,(K+hor+ver)*(K+hor+ver)-(K)*(K));
    }
    return 0;
    
}
