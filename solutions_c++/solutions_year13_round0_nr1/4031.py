#include <cstdlib>
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    FILE *stream;
	if((stream=freopen("A-large.in","r",stdin))==NULL)
		exit(-1);
	if((stream=freopen("output","w",stdout))==NULL)
		exit(-1);
		int t,i,counter=1,j,x=0,o=0,x2=0,o2=0,x3=0,o3=0,x4=0,o4=0,f;
		char tcase[4][4],c[1];
		cin>>t;
		gets(c);
        while(t>0)
        {
          for(i=0;i<4;i++)                    
          gets(tcase[i]);
          
          x3=o3=x4=o4=0;
          for(i=0;i<4;i++)  
           {  
              x=x2=o=o2=0;    
          for(j=0;j<4;j++)          
             {
          if(tcase[i][j]=='X'||tcase[i][j]=='T')
          x++;
          if(tcase[i][j]=='O'||tcase[i][j]=='T')
          o++;
          if(tcase[j][i]=='X'||tcase[j][i]=='T')
          x2++;
          if(tcase[j][i]=='O'||tcase[j][i]=='T')
          o2++;
          
          if(tcase[i][j]=='.')
          c[0]='.';
          
           if(i+j==3)
           {
           if(tcase[i][j]=='X'||tcase[i][j]=='T')
           x4++;
           if(tcase[i][j]=='O'||tcase[i][j]=='T')
           o4++;
           }
             }
             
             
            if(tcase[i][i]=='X'||tcase[i][i]=='T') 
            x3++;
            if(tcase[i][i]=='O'||tcase[i][i]=='T') 
            o3++;             
            
             
          if(x==4||x2==4||x3==4||x4==4)
          {
          cout<<"Case #"<<counter<<": X won";
          counter++;
          f=0;
          break;
          }
          else if(o==4||o2==4||o3==4||o4==4)
          {
          cout<<"Case #"<<counter<<": O won";
          counter++;
          f=0;
          break;
          }
          else
          {
            f=1;  
          }
               }
           if(f!=0&&c[0]=='.')
           cout<<"Case #"<<counter++<<": Game has not completed";
           else if(f==1)
           cout<<"Case #"<<counter++<<": Draw";

          
           t--; 
           if(t!=0)
           {
           gets(c);
           cout<<'\n';
           }
        }		
                  

    return EXIT_SUCCESS;
}

