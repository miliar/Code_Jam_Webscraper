#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
   using namespace std;

   int main()
   {

             freopen("W.in","r",stdin);
            freopen("W.out","w",stdout);

          int i,j,m,n,kase=1,p,q;
          char str1[600],str[600];
          char temp[600];

          int top=0,cnt;
          map<string,int>ab;

          scanf("%d",&m);



          while(m--)
          {
                    scanf("%d%d",&p,&q);

                    ab.clear();
                    getchar();

                    for(i=0;i<p;i++)
                    {        gets(str1);
                              ab[str1]=1;
                    }


                    cnt=0;

                    for(i=0;i<q;i++)
                    {
                              scanf("%s",str1);

                              top=0;

                              str[top++]=str1[0];
                              n=strlen(str1);

                              for(j=1;j<n;j++)
                              {
                                        if(str1[j]=='/')
                                        {
                                            str[top]='\0';
                                            strcpy(temp,str);

                                            if(ab[temp]!=1)
                                                  {cnt++;
                                                    ab[temp]=1;
                                                   }

                                           top=0;
                                            str[top++]=str1[j];
                                            break;
                                        }
                                        else str[top++]=str1[j];
                              }




                              for(j=j+1;j<n;j++)
                              {
                                        if(str1[j]=='/')
                                        {
                                                  str[top]='\0';
                                                  strcat(temp,str);

                                                  if(ab[temp]!=1)
                                                            {        cnt++;
                                                                      ab[temp]=1;

                                                            }
                                                  top=0;

                                                  str[top++]=str1[j];
                                        }
                                        else str[top++]=str1[j];
                              }

                              if(isalpha(str1[n-1])||isdigit(str1[n-1]))
                              {              str[top]='\0';

                                              strcat(temp,str);

                                              if(ab[temp]==0)
                                                { ab[temp]=1;
                                                   cnt++;
                                                }
                              }
                           memset(temp,'\0',sizeof(temp));

                    }

                    printf("Case #%d: %d\n",kase,cnt);
                    kase++;
                    cnt=0;
          }
          return 0;
    }
