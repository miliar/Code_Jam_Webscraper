#include <cstdio>
int t,n;
char inpc[1000]={0};
int main()
{
    FILE *fin,*fout;
    fin=fopen("in.txt","r");
    fout=fopen("out.txt","w");
    fscanf(fin,"%d",&t);
    for (int xht=1;xht<=t;xht++)
    {
        
        char ding[26][26]={0},boom[26][26]={0};
        fscanf(fin,"%d",&n);
        for (int xhn=0;xhn<n;xhn++)
        {
            fscanf(fin,"%s",inpc);
            ding[inpc[0]-'A'][inpc[1]-'A']=inpc[2];
            ding[inpc[1]-'A'][inpc[0]-'A']=inpc[2];
        }
        fscanf(fin,"%d",&n);
        for (int xhn=0;xhn<n;xhn++)
        {
            fscanf(fin,"%s",inpc);
            boom[inpc[0]-'A'][inpc[1]-'A']=1;
            boom[inpc[1]-'A'][inpc[0]-'A']=1;
        }
        fscanf(fin,"%d %s",&n,inpc);
        int ptr=0,lenn=0;
        char outc[1000]={'0'},foutc[1000]={'['};
        //printf("%s\n",inpc);
        for (int xhn=0;xhn<n;xhn++)
        {
            outc[ptr]=inpc[xhn];
            if (ptr!=0)
            {
               if (ding[outc[ptr]-'A'][outc[ptr-1]-'A']!=0)
               {
                  ptr--;
                  outc[ptr]=ding[outc[ptr]-'A'][outc[ptr+1]-'A'];
               }
            }
            if (ptr!=0)
            {
               for (int xhb=0;xhb<ptr;xhb++)
               if (boom[outc[ptr]-'A'][outc[xhb]-'A']!=0)
               {
                  ptr=-1;
               }
            }
            ptr++;
            outc[ptr]='\0';
            //printf("Test-%d %s %d\n",xht,outc,ptr);
        }
        lenn=ptr;ptr=1;
        for (int xhn=0;xhn<lenn;xhn++)
        {
            foutc[ptr++]=outc[xhn];
            foutc[ptr++]=',';
            foutc[ptr++]=' ';
        }
        if(foutc[ptr-1]==' ')ptr-=2;
        foutc[ptr++]=']';
        foutc[ptr++]='\0';
        fprintf(fout,"Case #%d: %s\n",xht,foutc);
    }
    fclose(fin);
    fclose(fout);
    //scanf("%d",&t);
    return 0;
}
            
            
            
