#include <fstream>
#define N 50
using namespace std;

char rot[N][N];

bool kinarow(int n,int k,char c)
{
    //row checking
    int num,i,j,a;
    for(i=0;i<n;i++)
    {
        num=0;
        for(j=0;j<n;j++)
        {
            if(rot[i][j]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }
    for(j=0;j<n;j++)
    {
        num=0;
        for(i=0;i<n;i++)
        {
            if(rot[i][j]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }
    //row and col done
    //now diagonal
    for(i=0;i<n;i++)
    {
        num=0;
        for(a=0;a<=i;a++)
        {
            if(rot[i-a][a]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }
    for(i=0;i<n;i++)
    {
        num=0;
        for(a=0;a<=i;a++)
        {
            if(rot[i-a][n-1-a]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }


    for(j=0;j<n;j++)
    {
        num=0;
        for(a=0;a<=j;a++)
        {
            if(rot[n-1-a][j-a]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }

    for(j=0;j<n;j++)
    {
        num=0;
        for(a=n-1;a>=j;a--)
        {
            if(rot[a][j+n-1-a]==c)
                num++;
            else
                num=0;
            if(num==k)
                return true;
        }
    }
    return false;
}

int main()
{
    FILE *fp,*out;
    fp=fopen("A-large.in","r");
    out=fopen("A-largeOut.out","w");
    int t,p,i,j,k,n,a,b;
    char c;
    fscanf(fp,"%d",&t);
    char arr[N][N];
    bool red,blue;
    for(p=0;p<t;p++)
    {
        fscanf(fp,"%d%d\n",&n,&k);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                fscanf(fp,"%c",&arr[i][j]);
            }
            fscanf(fp,"%c",&c);
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                rot[j][n-i-1]=arr[i][j];
            }
        }
        //rotation done.... now gravity
        for(j=0;j<n;j++)
        {
            /*for(a=n-1;a>=0;a--)
            {
                if(rot[a][j]=='R'||rot[a][j]=='B')
                {
                    break;
                }
            }
            for(i=0;i<=a;i++)
            {
                rot[n-i-1][j]=rot[a-i][j];
            }
            for(;i<n;i++)
            {
                rot[n-i-1][j]='.';
            }*/
            a=n-1;
            for(i=n-1;i>=0;i--)
            {
                while(a>=0&&rot[a][j]=='.')
                {
                    a--;
                }
                if(a<0)
                    break;
                rot[i][j]=rot[a][j];
                a--;
            }
            for(;i>=0;i--)
                rot[i][j]='.';
        }
        red=kinarow(n,k,'R');
        blue=kinarow(n,k,'B');

        printf("\n");
        if(red&&blue)
        {
            fprintf(out,"Case #%d: Both\n",p+1);
        }
        else if(red)
        {
            fprintf(out,"Case #%d: Red\n",p+1);
        }
        else if(blue)
        {
            fprintf(out,"Case #%d: Blue\n",p+1);
        }
        else
        {
            fprintf(out,"Case #%d: Neither\n",p+1);
        }
    }
    fclose(fp);
    fclose(out);
    return 0;
}
