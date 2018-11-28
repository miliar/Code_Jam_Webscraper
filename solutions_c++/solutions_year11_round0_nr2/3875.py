#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    int t,c,d,i,j,n,flagc=0,flagd=0,k,flag=0;
    char strc[3],strd[2],str[11],str2[101][11];
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>c;
        if(c>0)
        {
            flagc=1;
            cin>>strc;
        }
        cin>>d;
        if(d>0)
        {
            flagd=1;
            cin>>strd;
        }

        cin>>n;
        cin>>str;
        k=0;
        str2[i][k]='$';

        for(j=0;j<n;j++)
        {
            if(flagc==0 && flagd==0)
            {
                str2[i][k++]=str[j];
            }
            else if(flagc==1 && flagd==0)
            {
                if(j==0)
                    str2[i][k++]=str[j];
                else
                {
                    if((str[j]==strc[0] && str2[i][k-1]==strc[1])||(str[j]==strc[1] && str2[i][k-1]==strc[0]))
                    {
                        str2[i][k-1]=strc[2];
                    }
                    else
                    {
                        str2[i][k++]=str[j];
                    }

                }
            }
            else if(flagd==1 && flagc==0)
            {
               if(str2[i][k]=='$')
                    str2[i][k++]=str[j];
                else
                {
                    flag=0;
                    if(str[j]==strd[0])
                    {
                        for(int m=0;m<k;m++)
                        {
                            if(str2[i][m]==strd[1])
                            {
                                k=0;
                                str2[i][k]=='$';
                                flag=1;
                                break;
                            }
                            else{}
                        }
                        if(flag==0)
                            str2[i][k++]=str[j];

                    }
                    else if(str[j]==strd[1])
                    {
                        for(int m=0;m<k;m++)
                        {
                            if(str2[i][m]==strd[0])
                            {
                                k=0;
                                str2[i][k]=='$';
                                flag=1;
                                break;
                            }
                            else{}
                        }
                        if(flag==0)
                            str2[i][k++]=str[j];
                    }
                    else
                    {
                        str2[i][k++]=str[j];
                    }
                }
            }
            else
            {
                if(str2[i][k]=='$')
                    str2[i][k++]=str[j];
                else
                {
                    flag=0;
                    if((str[j]==strc[0] && str2[i][k-1]==strc[1])||(str[j]==strc[1] && str2[i][k-1]==strc[0]))
                    {
                        str2[i][k-1]=strc[2];
                    }
                    else if(str[j]==strd[0])
                    {
                        //flag=0;
                        for(int m=0;m<k;m++)
                        {
                            if(str2[i][m]==strd[1])
                            {
                                k=0;
                                str2[i][k]=='$';
                                flag=1;
                                break;
                            }
                            else{}

                        }
                        if(flag==0)
                                str2[i][k++]=str[j];

                    }
                    else if(str[j]==strd[1])
                    {
                        for(int m=0;m<k;m++)
                        {
                            if(str2[i][m]==strd[0])
                            {
                                k=0;
                                str2[i][k]=='$';
                                flag=1;
                                break;
                            }
                            else{}
                        }
                        if(flag==0)
                                str2[i][k++]=str[j];
                    }
                    else
                    {
                        str2[i][k++]=str[j];
                    }
                }
            }

        }
        str2[i][k]='\0';

    }

    for(i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": [";
        j=0;
        if(str2[i][j]=='\0')
            cout<<"]"<<endl;
        else
        {

        while(str2[i][j+1]!='\0')
        {
            cout<<str2[i][j]<<", ";
            j++;
        }
        cout<<str2[i][j]<<"]"<<endl;
        }
    }
    return 0;

}
