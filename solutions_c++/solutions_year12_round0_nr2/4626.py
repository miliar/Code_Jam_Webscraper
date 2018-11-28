#include <cstdlib>
#include <iostream>

using namespace std;

int jg;
int t,n,s,p;
int** ww;
int* hx;

int** hh(int *l,int size)
{
    int** re;
    re = new int*[2];
    re[0] = new int[size];
    re[1] = new int[size];
    
    for(int i=0;i<size;i++)
    {               
        int gc = l[i];  
         
        int ma;                    // not surprise
         int d = gc/3;
                int w = gc%3;
                if(w == 0)
                {
                    ma = d;
                }
                if(w == 1)
                {
                    ma = d+1;
                }
                if(w == 2)
                {
                    ma = d+1;
                }
                re[0][i] = ma;
                
                 
                 if(gc<=1 || gc>=29)
        {
            re[1][i] = -1;
            continue;
        }       
                                              //surprised
                if(w == 0)
                {
                    ma = d+1;
                }
                if(w == 1)
                {
                    ma = d+1;
                }
                if(w == 2)
                {
                    if(d<=8)
                    ma = d+2;
                    else
                    ma = -1;
                }
                re[1][i] = ma;
                
    }
    return re;
}


void dg(int f,int cas,int mn)
{
    if(f == s)
    {
        int sjg = 0;
        for(int i=0;i<n;i++)
        {
            if(ww[hx[i]][i]>=p)
            sjg++;
        }
        if(sjg>jg)
        jg = sjg;
        //hx[mn-1] = 0;
        return;
    }
    for(int i=mn;i<n;i++)
    {
        hx[i] = 1;
        dg(f+1,cas,i+1);
        hx[i] = 0;
    }
}

/*void zh()
{
    int hx[n];
    for(int i=0;i<n;i++)
    hx[i] = 0;
    dg(0,cas,0);
    
}

*/




int main(int argc, char *argv[])
{
    FILE *fin  = fopen ("B-small-attempt1.in", "r");
	FILE *fout = fopen ("B-small-attempt1.out", "w"); 
	
	fscanf(fin,"%d",&t);
	
	for(int i=0;i<t;i++)
	{
        fscanf(fin,"%d",&n);
        fscanf(fin,"%d",&s);
        fscanf(fin,"%d",&p);
        
        jg = 0;
        
        int gc[n];
        for(int j=0;j<n;j++)
        {
            fscanf(fin,"%d",&gc[j]);
        }
        
        ww = hh(gc,n);
        
        
        hx = new int[n];
    for(int k=0;k<n;k++)
    hx[k] = 0;
    dg(0,i,0);
    fprintf(fout,"Case #%d: %d\n",i+1,jg);
        
        
        
        
        
        
       /* 
        if(n == 1)
        {
            
            if(s == 0)
            {
                if(ww[0][0]>=p)
                fprintf(fout,"Case #%d: 1",i);
                else
                fprintf(fout,"Case #%d: 0",i);
                
            }
            if(s == 1)
            {
                if(ww[1][0]>=p)
                fprintf(fout,"Case #%d: 1",i);
                else
                fprintf(fout,"Case #%d: 0",i);
            }
            
        }
        
        
        */
        
        
        
    }
    
    
  
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
