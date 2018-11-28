#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int t,a,b;
int jg;

int hx[10100];

string sa,sb;

void rec(string zz)
{
    memset(hx,0,10100*4);
    
    string z = zz;
    int co = z.length();
    int lz = z.length();
    //cout<<"co: "<<co<<"\n";
    while(--co)
    {
        
        
        string tmp;
        tmp.append(z,1,lz-1);
        tmp.append(z,0,1);
        z = tmp;
      
        
        
        if((z.compare(zz) >0) && (z.compare(sb)<=0))
        {
            
            int hhx = 0;
            int i=0;
            while(i<lz-1)
            {
                hhx = (hhx+(int)z[i]-48)*10;
                i++;
            }
            hhx = hhx+(int)z[lz-1]-48;
            if(hx[hhx] == 1)
            continue;
            hx[hhx] = 1;
            jg++;
            //cout<<"sa: "<<sa;
        //cout<<"zz: "<<zz;
        //cout<<"z: "<<z;
        //cout<<"while: ";
        //cout<<"sb: "<<sb;
         //   cout<<"manzu\n";cout<<z.compare(zz)<<endl;
            //cout<<"rec: "<<zz;//
            //return true;
        }
        
    }
    
   
}


int main(int argc, char *argv[])
{
    
    FILE *fin  = fopen ("C-small-attempt0.in", "r");
	FILE *fout = fopen ("C-small-attempt0.out", "w"); 
	
	
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
        jg = 0;
        fscanf(fin,"%d",&a);
        fscanf(fin,"%d",&b);
        
        if(b <= 10)
        {
           fprintf(fout,"Case #%d: 0\n",i+1); 
           continue;
        }
        
        int bb = b;
        //int ss = 0;
        string ww;
        while(bb != 0)
            {
                ww.push_back( bb%10+48);//cout<<bb%10;
                bb/=10;//
            }
        sb.clear();  
        int nww = ww.length();
        for(int l=nww-1;l>=0;l--) 
        {
            sb.push_back(ww[l]);
        } 
        //cout<<sb;//cout<<"ok";
        
        int aaa = a-1;
        
        while(aaa<b)
        {
            aaa++;
            int aa = aaa;
           
            //ss = 0;
            string wa;
            while(aa != 0)
            {
                wa.push_back( aa%10+48);
                aa/=10;
            }
            int na = wa.length();
            sa.clear();
            for(int l=na-1;l>=0;l--)
            {
                sa.push_back(wa[l]);
            }
           //cout<<sa<<' ';
           //cout<<sb<<endl;
            
            //if(rec(sa))
            rec(sa);
            //jg++;
           // cout<<"ok";system("PAUSE");
        }
        
       fprintf(fout,"Case #%d: %d\n",i+1,jg); 
        
     
        
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
