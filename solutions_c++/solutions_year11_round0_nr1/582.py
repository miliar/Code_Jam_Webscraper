#include<iostream>
#include<vector>

using namespace std;

#define calc(a) (a > 0 ? (a) : 0)

FILE *fp;
FILE *fp2;

int T,n,ans;


int solve(vector<int> x,vector<int> color)
{
    int ret = 0;
    int posO = 1,posB = 1,freetimeO = 0,freetimeB = 0;
    for(int i = 0;i < x.size();++i)
    {
        if(color[i] == 'O')
        {
            if(posO == x[i])
            {
                freetimeO = 0;
                ++ret;
                ++freetimeB;    
            }else{
                int dist = x[i] - posO;   
                if(dist < 0)
                    dist = 0 - dist;
                dist = calc(dist - freetimeO);
                ret += dist;
                freetimeB += dist;
                
                freetimeO = 0;
                ++ret;
                ++freetimeB;  
            }
            posO = x[i];
        }else{
            if(posB == x[i])
            {
                freetimeB = 0;
                ++ret;
                ++freetimeO;    
            }else{
                int dist = x[i] - posB;   
                if(dist < 0)
                    dist = 0 - dist;
                dist = calc(dist - freetimeB);
                ret += dist;
                freetimeO += dist;
                
                freetimeB = 0;
                ++ret;
                ++freetimeO;  
            }       
            posB = x[i];     
        }
       
    }
    return ret;    
}

int main()
{
    fp = fopen("testin.txt","r");
    fp2 = fopen("out.txt","w");
    fscanf(fp,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        vector<int> a;
        vector<int> b;
        fscanf(fp,"%d",&n);
        for(int j = 1;j <= n;++j)
        {
            char t;
            do{
                fscanf(fp,"%c",&t);
            }while(t != 'O' && t != 'B');
            int temp;
            fscanf(fp,"%d",&temp);
            a.push_back(temp);
            b.push_back(t);
        }    
        ans = solve(a,b);
        fprintf(fp2,"Case #%d: %d\n",i,ans);
    }
    fclose(fp);
    fclose(fp2);
    return 0;    
}
