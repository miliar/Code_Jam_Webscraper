#include<iostream>
#include<string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    string rep[40],cls[30],str,key;
    int t,c,d,n,i,j,k;
    int num = 1;
    scanf("%d",&t);
    while(t--)
    {
        key = "";
        scanf("%d",&c);
        for(i=0;i<c;i++) 
        cin >> rep[i];
        scanf("%d",&d);
        for(i=0;i<d;i++)
         cin >> cls[i];
        scanf("%d",&n);
        cin >> str;
        int len = 0;
        for(i=0;i<n;i++)
        {
            key+=str[i];
            len+=1;
            if(key.length()>=2)
            {
                if(c)
                {
                   for(j=0;j<c;j++)
                   {
                       if( (rep[j][0]==key[len-2]&&rep[j][1]==key[len-1]) || (rep[j][1]==key[len-2] && rep[j][0]==key[len-1]))
                       {
                            key.erase(len-2,2);
                            key+=rep[j][2];
                            len-=1;
                            break;
                       }
                   }
                }
               
               if(d)
               {
                    int flag = 1;
                    for(j=0;j<d;j++)
                    {
                        for(k=0;k<key.length()-1;k++)
                        {
                            if((key[len-1]==cls[j][0]&&key[k]==cls[j][1])||(key[k]==cls[j][0]&&key[len-1]==cls[j][1]))
                            {
                                key="";
                                len = 0;
                                flag = 0;
                                break;
                            }
                       }
                       if(flag==0) break;
                   }
               }
            }
        }
        
        if(key.length()==0)
         printf("Case #%d: []\n",num++);
        else if(key.length()==1)
         cout << "Case #"<< num++ <<": [" << key[0] <<"]"<<endl;
        else
        {
            cout << "Case #"<< num++ << ": [" << key[0]<<",";
            for(i=1;i<key.length()-1;i++)
               cout << " "<<key[i]<<",";
            cout << " " << key[key.length()-1]<<"]"<<endl;
        }
    }
    return 0;
}
