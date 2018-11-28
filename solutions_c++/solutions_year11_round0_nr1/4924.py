# include <iostream>
# include <fstream>
using namespace std;
# include <stdio.h>
# include <math.h>


int abs(int a)
{
    if(a>=0)
    return a;
    else
    a=a*(-1);
    return a;
}


int main()
{
    int total,t;
    cin>>t;
    int k,n,out[t],value,i,moves,j,orange_curr,orange_last,blue_last,blue_curr;
    char ch;
    int array[40];
    for(i=1;i<=t;i++)
    {
        scanf("%d\n",&n);
        total=0;
        k=0;
        for(j=0;j<n;j++)
        {
            scanf(" %c %d",&ch,&value);
            if(ch=='O')
            {
                array[k++]=0;
            }
            else if(ch=='B')
            array[k++]=1;
            array[k++]=value;
        }
        /*
        for(j=0;j<k;j++)
        {
            cout<<array[j]<<' ';
        }
        */
        orange_curr=1;
        blue_curr=1;
        orange_last=0;
        blue_last=0;
        moves=0;
        for(j=0;j<k;j+=2)
        {
            if(array[j]==0)
            {
                moves=abs(array[j+1]-orange_curr);
                orange_curr=array[j+1];
                if(moves<=(total-orange_last))
                moves=0;
                else
                moves=moves-(total-orange_last);
                total=total+moves+1;
                orange_last=total;
            }


            else if(array[j]==1)
            {
                moves=abs(array[j+1]-blue_curr);
                blue_curr=array[j+1];
                if(moves<=(total-blue_last))
                moves=0;
                else
                moves=moves-(total-blue_last);
                total=total+moves+1;
                blue_last=total;
            }
        }

        out[i]=total;
    }
    // ofstream ofile;
    // ofile.open("output.txt",ios::out);
    /*
    for(i=1;i<=t;i++)
    {


        ofile.put('C');
        ofile.put('a');
        ofile.put('s');
        ofile.put('e');
        ofile.put('#');
        temp=i;
        l=0;
        while(temp)
        {
            str[l]=48+(temp%10);
            l++;
            temp/=10;
        }
        for(j=l-1; j>=0;j--)
        {
            ofile.put(str[j]);
        }
        ofile.put(ch);
        ofile.put(':');
        ofile.put(' ');
        temp=out[i];
        l=0;
        while(temp)
        {
            str[l]=48+(temp%10);
            l++;
            temp/=10;
        }
        for(j=l-1; j>=0;j--)
        {
            ofile.put(str[j]);
        }
        ofile.put('\n');

    }
    */
    for(i=1;i<=t;i++)
    {
        cout<<"Case# "<<i<<": "<<out[i]<<endl;
    }
    // ofile.close();



    return 0;
}











