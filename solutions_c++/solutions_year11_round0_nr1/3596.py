#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<stack>

using namespace std;

vector<pair<char, int> >v;
//vector<int > va;
//vector<int > vb;
int main(void){
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    char a = 'O',b = 'B';
     
    for(int t = 0; t<T; t++)
    {
        int n;
        scanf("%d",&n);
        //getchar();
        char ch[5];
        int num;
        int sum = 0;
        for(int i = 0; i<n; i++)
        {
            scanf("%s%d",&ch,&num);
            v.push_back(make_pair(ch[0],num));
            /*if(ch[0] == a)
                va.push_back(num);
            else
                vb.push_back(num);*/
        }
        //int x = 0,y = 0; // Position of a nad b respectively
        
        int la = 1, lb = 1;
        int lastPos = 1;
        sum = v[0].second - lastPos + 1;
        char lastChar = v[0].first;
        lastPos = v[0].second;
        
        if(lastChar == a)
        {
            la = lastPos;
            //x++;
        }
        else
        {
            lb = lastPos;
            //y++;
        }
        
        int sumArr[105],sumA[105];
        sumArr[0] = sum;
        sumA[0] = sum;
        for(int i = 1; i<v.size(); i++)
        {
            int curPos = v[i].second;
            if(lastChar == v[i].first)
            {
                sum += (abs(curPos - lastPos) + 1);
            }
            else
            {
                if(lastChar == a)   // Means that current char is b
                {
                    int needToGo = (int)abs(lb - curPos);
                    int sumFac = sumArr[i - 1];
                    
                    if(i > 1 && v[i - 2].first == a)
                    {
                        int j = i - 1;
                        while(j > 0 && v[j - 1].first == a)
                        {
                            sumFac += sumArr[j - 1];
                            j--;
                        }
                    }
                    
                    int alreadyGone = min(sumFac,needToGo);
                    if(needToGo > alreadyGone)
                    {
                        sum += (needToGo - alreadyGone);
                    }
                    //printf("Char = %c, sumFac = %d, last = %d\n",'B',sumFac,lastPos);
                    sum += 1;
                    
                    lastChar = b; 
                }
                else if(lastChar == b) // means that current char is o
                {
                    int needToGo = (int)abs(la - curPos);
                    int sumFac = sumArr[i - 1];
                    
                    if(i > 1 && v[i - 2].first == b)
                    {
                        int j = i - 1;
                        while(j > 0 && v[j - 1].first == b)
                        {
                            sumFac += sumArr[j - 1];
                            j--;
                        }
                    }
                    
                    //printf("Char = %c, sumFac = %d, last = %d\n",'O',sumFac,lastPos);
                    
                    int alreadyGone = min(sumFac,needToGo);
                    if(needToGo > alreadyGone)
                    {
                        sum += (needToGo - alreadyGone);
                    }
                    sum += 1;
                    lastChar = a; 
                }
            }
            
            lastPos = curPos;
            
            if(lastChar == a)
            {
                la = lastPos;
                //x++;
            }
            else
            {
                lb = lastPos;
                //y++;
            }
            sumA[i] = sum;
            sumArr[i] = sum - sumA[i - 1];
            //printf("***sum = %d, sumArr[i] = %d\n",sum,sumArr[i]);
        }
        printf("Case #%d: %d\n",t+1, sum);
        v.clear();
    }
    return 0;
}
