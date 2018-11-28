#include<iostream>
#include<fstream>
using namespace std;
int tcase,n,num;
int a[50];

ofstream fout("B-large.out");
ifstream fin("B-large.in");

void qsort(int l,int r)
{
     int i,j,k,l1,r1,m;
     l1=l;r1=r;m=a[l];
     while (l1<=r1)
     {
           while (a[l1]<m) l1++;
           while (a[r1]>m) r1--;
           if (l1<=r1) 
           {i=a[l1];a[l1]=a[r1];a[r1]=i;
            l1++;r1--;}
     }
     if (l1<r) qsort(l1,r);
     if (l<r1) qsort(l,r1);     
}

int main()
{
    int i,j,k,l;
    char s[256];
    char c;
    fin>>tcase;fin.getline(s,256);
    for (i=1;i<=tcase;i++)    
    {
        num=0;
        fin.getline(s,256);
        memset(a,0,sizeof(a));
        for (j=0;j<strlen(s);j++)
        {
              num++;a[num]=(int)(s[j])-(int)('0');              
        }
        j=num;k=a[j];
        while (j>0)
        {
              j--;
              if (j>0){if (a[j]<k) break;}
              k=a[j];
        }        
        
        if (j>0)
        {
                l=j+1;
                for (k=j+1;k<=num;k++) 
                    if (a[k]>a[j] && a[k]<a[l]) l=k;
                int ll;
                ll=a[j];a[j]=a[l];a[l]=ll;
                qsort(j+1,num);
                fout<<"Case #"<<i<<": ";
                for (k=1;k<=num;k++) fout<<a[k];
                fout<<endl;
        }
        else if (j==0)
        {
             l=1;
             for (k=1;k<=num;k++) 
                 if (a[k]>0 && a[k]<a[l]) l=k;
             int ll;
                ll=a[1];a[1]=a[l];a[l]=ll;
             qsort(2,num);
             fout<<"Case #"<<i<<": "<<a[1]<<"0";
             for (k=2;k<=num;k++) fout<<a[k];
             fout<<endl;
        }
    }
    //cin>>i;
    return 0;
}
