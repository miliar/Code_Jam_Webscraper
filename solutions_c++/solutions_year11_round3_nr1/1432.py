#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int T;
    cin>>T;
    
    for(int l=1;l<=T;l++)
    {
        int R,C;
        cin>>R>>C;
        
        char **pic;
        int i,j;
        pic=new char*[R];
        for(i=0;i<R;i++)
            pic[i]=new char[C];
        
        bool flag=true;
        int tot,col;
        for(i=0,tot=0;i<R;i++)
        {
            for(j=0,col=0;j<C;j++)
            {
                cin>>pic[i][j];
                if(pic[i][j]=='#')
                {
                    col++;
                    tot++;
                }
            }
            if(col%2!=0)
                flag=false;
        }
        if(tot%4!=0)
            flag=false;
        
        if(flag==true)
        {
            for(i=0;i<R-1;i++)
            {
                for(j=0;j<C-1;j++)
                {
                    if(pic[i][j]=='#')
                    {
                        if(pic[i+1][j]=='#'&&pic[i][j+1]=='#'&&pic[i+1][j+1]=='#')
                        {
                            pic[i][j]='/';
                            pic[i+1][j]='\\';
                            pic[i][j+1]='\\';
                            pic[i+1][j+1]='/';
                        }
                    }
                }
            }
            for(i=0;i<R&&flag==true;i++)
                for(j=0;j<C&&flag==true;j++)
                    if(pic[i][j]=='#')
                        flag=false;
        }
        
        cout<<"Case #"<<l<<":\n";
        if(flag==false)
            cout<<"Impossible\n";
        else
            for(i=0;i<R;i++)
            {
                for(j=0;j<C;j++)
                    cout<<pic[i][j];
                cout<<endl;
            }
    }
    
    return 0;
}
