#include<iostream.h>
#include<fstream.h>


int main()
{
	ifstream fin;fin.open("data.in",ios::in);
	ofstream fout;fout.open("data.out",ios::out);

 int z;
 fin>>z;
 for(int i=0;i<z;i++)
 {
 	fout<<"Case #"<<(i+1)<<": ";
      int n,s,p,max=0;
      fin>>n>>s>>p;

      int g[101];
      for(int j=0;j<n;j++)
      {fin>>g[j];
       if(g[j]/3 >=p)
       {g[j]=0;
       max++;}
       else if(g[j]/3==p-1 && g[j]%3>=1)
       {g[j]=0;max++;}
      }


      while(s!=0)
      {
        for(int k=0;k<n;k++)
        {
         if(g[k]!=0)
         {
           if ( ( (g[k]/3)==p-2) && ((g[k]%3) ==2) || (g[k]/3)==p-1)
           {
            g[k]=0;
            s--;
            max++;
           }
         }
        }

      }





        fout<<max;
        fout<<endl;

 }

}

