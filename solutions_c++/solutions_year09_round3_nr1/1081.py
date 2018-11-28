#include<iostream>
#include<fstream>
#include<string>
#include<math.h>

//#define fin cin
//#define fout cout

using namespace std;

int ans[19];
unsigned long long int answer=0;

void extract(char *s1, const char*s2)
{
    int i,j,k=1,l=strlen(s2);
    
    char ch = s2[0];
    strcpy(s1, "");
    
    strcat(s1,&ch);
    
    for(i=1;i<l;i++)
    {
        for(j=0;j<k;j++)
        if( s1[j]==s2[i] )
        break;
        
        if(j==k)
        s1[k++]=s2[i];
    }  
    
          s1[k] = '\0';      
}

/*void calc(int x)
{
    int i=18,temp,carry=0;
    while(x>0)
    {
        temp = x%10 + carry + ans[i];
        ans[i--] = temp%10;
        carry = temp/10;
        x /= 10;
    }    
} */   

int main()
{
    int *a,i,j,k,n,ls,lu,tv;
    char *s = new char[61],*u = new char[61],*v = new char[61];
    
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small1.out");
    
    if(!fin || !fout)
    {
        cout<<"Error!!!";
        cin>>n;
        return 1;
    }
    
    fin>>n;
    
    for(i=0;i<n;i++)
    {
       /* for(j=0;j<19;j++)
        ans[j]=0; */
        
       
        answer = 0;
        
        fin>>s;
        ls = strlen(s);
        
        for(j=0;j<ls-1;j++)
        if(s[j]!=s[j+1])
        break;
        
        if(j==ls-1)
        {
            for(j=0;j<ls;j++)
            answer += (unsigned long long)pow(2.0,double(j));
            fout<<"Case #"<<i+1<<": "<<answer<<endl;
            continue;
        }    
        
        extract(u,s);
        lu = strlen(u);
        
        
        for(j=0;j<lu;j++)
        {
            tv = ( j==0 ? 1 : ( j==1 ? 0 : j) );
            
            for(k=0;k<ls;k++)
            if( s[k]==u[j] )
            v[k] = (tv+48);
        }
        
        v[ls] = '\0';
        
        for(j=ls-1;j>=0;j--)
        {
            tv = int( pow( double(lu), double(ls-1-j) ) );
            //calc( (v[j]-48) * tv );
            answer += (v[j]-48)*tv;
        }    
        
        /*for(j=0;j<19 && ans[j]==0;j++);
        
        fout<<"Case #"<<i+1<<": ";
        
        for(k=j;k<19;k++)
        fout<<ans[k];*/
        
        fout<<"Case #"<<i+1<<": "<<answer<<endl;
    }
    
    fin.close();
    fout.close();
}        
