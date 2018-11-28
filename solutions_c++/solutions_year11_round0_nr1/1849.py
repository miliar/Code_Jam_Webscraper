#include <cstdio>
int n,t,r[100],k[100];
int gnt(int nt,int whichr)
{
    int xhk;
    for (xhk=nt+1;xhk<n;xhk++)
        if (r[xhk]==whichr)
           break;
    return xhk;
}
int main()
{
    FILE *fin,*fout;
    fin=fopen("in.txt","r");
    fout=fopen("out.txt","w");
    char inp[3];
    fscanf(fin,"%d",&t);
    for (int xht=0;xht<t;xht++)
    {
        int ntk[2]={-1,-1},tt=0,np[2]={1,1};
        fscanf(fin,"%d",&n);
        
        for (int xhn=0;xhn<n;xhn++)
        {
            fscanf(fin,"%s",&inp);
            r[xhn]=(inp[0]=='O'?0:1);
            fscanf(fin,"%d",&k[xhn]);
        }
        
        ntk[0]=gnt(ntk[0],0);
        ntk[1]=gnt(ntk[1],1);
        while (ntk[0]!=n||ntk[1]!=n)
        {
              tt++;
              int gntk[2]={0};
              for (int xhr=0;xhr<2;xhr++)
              {
                  if (k[ntk[xhr]]!=np[xhr])
                     {if(k[ntk[xhr]]>np[xhr])np[xhr]++;else np[xhr]--;}
                  else
                      if (ntk[xhr]<ntk[1-xhr])
                         gntk[xhr]=1;   
              }
              for (int xhr=0;xhr<2;xhr++)
                  if(gntk[xhr]==1)ntk[xhr]=gnt(ntk[xhr],xhr);
              //printf("test%d orange-%d->%d,blue-%d->%d time=%d\n",xht,np[0],ntk[0],np[1],ntk[1],tt);
        }
        fprintf(fout,"Case #%d: %d\n",xht+1,tt);
    }
    fclose(fin);
    fclose(fout);
    //scanf("%d",&n);
    return 0;
}
        
