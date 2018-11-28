#include<iostream>
using namespace std;

int theMin(int a,int b,int c,int d,int& min)
{
    int who=0;
    min=a;
    if(b<min)
    {
      min=b;
      who=1;
    }
    if(c<min)
    {
      min=c;
      who=2;
    }
    if(d<min)
    {
      min=d;
      who=3;
    }
      
    return who;   
}
void output(int** map,int H,int W,int line,FILE* out)
{
	// cout<<line<<endl;
	 //cout<<H<<" "<<W<<endl;
     int** label=new int*[H];
     for(int i=1;i<H-1;i++)
     {
         label[i]=new int[W];
         for(int j=1;j<W-1;j++)
           label[i][j]=-1;
     }
     
     int color[10000];
     for(i=0;i<10000;i++)
       color[i]=-1;
       
     int x=0;
     for(i=1;i<H-1;i++)
     for(int j=1;j<W-1;j++)
     {
        if(label[i][j]==-1)
          label[i][j]=x++;
        int min;
        int who=theMin(map[i-1][j],map[i][j-1],map[i][j+1],map[i+1][j],min);
	//	cout<<"5"<<endl;
        if(min<map[i][j])
        {
			
            if(who==0)
            {   
			//	cout<<"1"<<endl;
                if(label[i][j]>label[i-1][j])
                  color[label[i][j]]=label[i-1][j];
                else if(label[i][j]<label[i-1][j])
                  color[label[i-1][j]]=label[i][j];
            }
            else if(who==1)
            {
			//	 cout<<"2"<<endl;
			//	 cout<<i<<" "<<j<<endl;
			//	 cout<<label[i][j]<<" "<<label[i][j-1];
                 if(label[i][j]>label[i][j-1])
                   color[label[i][j]]=label[i][j-1];
                 else if(label[i][j]<label[i][j-1])
                   color[label[i][j-1]]=label[i][j];
            }
			
            else if(who==2)
            {
				//  cout<<"3"<<endl;
                  if(label[i][j+1]==-1)
                    label[i][j+1]=label[i][j];
                  else if(label[i][j]>label[i][j+1])
                    color[label[i][j]]=label[i][j+1];
                  else if(label[i][j]<label[i][j+1])
                    color[label[i][j+1]]=label[i][j];
            }
            else
            {
			//	 cout<<"4"<<endl;
                 label[i+1][j]=label[i][j];
            }
            
            
        }
        
        
     }
     
     int* colorShow=new int[x];
     int y=0;
     for(i=0;i<x;i++)
     {
         if(color[i]==-1)
           colorShow[i]=y++;
         else
           colorShow[i]=colorShow[color[i]];
     }

     

     fputs("Case #",out);
     char buf[5];
     itoa(line,buf,10);
     fputs(buf,out);
     fputs(":",out);
     fputc('\n',out);
     
     for(i=1;i<H-1;i++)
     {
       char ch;
       int j;
       for(j=1;j<W-2;j++)
       {
          
          ch='a'+colorShow[label[i][j]];
          fputc(ch,out);
          fputs(" ",out);
       }
       ch='a'+colorShow[label[i][j]];
       fputc(ch,out);
       fputc('\n',out);
     }

	 for(i=1;i<H-1;i++)
     {
         delete[] label[i]; 
     }

	 delete[] label;
       
}


int main()
{
    FILE* in=fopen("B-small-attempt3.in","r");
    FILE* out=fopen("B-small-attempt3.out","w");
    
    char buf[500];
    
    fgets(buf,500,in);
    int n=atoi(buf);
    
    for(int line=1;line<=n;line++)
    {
        fgets(buf,500,in);
        char* p=buf;
        char* mark=buf;
        while(*p!=' ')
          p++;
        *p='\0';
        
        int H=atoi(mark);
        mark=++p;
        
        while(*p!='\n')
          p++;
        *p='\0';
        int W=atoi(mark);
        
        int** map=new int*[H+2];
        for(int i=0;i<H+2;i++)
        {
           map[i]=new int[W+2];
           map[i][0]=map[i][W+1]=10000;
           if((i==0)||(i==H+1))
           {
              for(int j=0;j<W+2;j++)
                map[i][j]=10000;
           }
        }

		
        for(i=1;i<=H;i++)
        {
           fgets(buf,500,in);
           p=buf;
           mark=buf;
           int j;
           for(j=1;j<W;j++)
           {
              while(*p!=' ')
               p++;
              *p='\0';
              map[i][j]=atoi(mark);
              mark=++p;
           }
           while(*p!='\n')
             p++;
           *p='\0';
           map[i][j]=atoi(mark);
        }
      /*  for(i=0;i<H+2;i++)
		{
          for(int j=0;j<W+1;j++)
		  {
			cout<<map[i][j]<<" ";
		  }
		  cout<<map[i][j]<<endl;
		}*/
        
        output(map,H+2,W+2,line,out);
        
        for(i=0;i<H+2;i++)
        {
           delete[] map[i]; 
        }
        
        delete[] map;
        
    }
    
    fclose(in);
    fclose(out);
    return 0;
}
