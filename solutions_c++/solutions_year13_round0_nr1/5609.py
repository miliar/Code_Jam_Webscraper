#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
char arr[5][5];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
   	freopen("out2.out","w",stdout);
    int t;
        cin >> t;
        
        char color;
        for(int k=1 ; k<=t ; k++)
        {
                bool f = 0;
                bool wonrow[] = {0,0,0,0};
                bool wonclm[] = {0,0,0,0};
                bool wrb[] = {0,0};
                bool someonewin = 0;
                bool therearepoints = 0;
                bool wrbflag = 0;
                for(int i=0 ; i<4 ; i++)
                cin >> arr[i];
                
                // ÚÔÇä ÇÔæÝ ÍÏ ÝÇÒ ÈÇáÕÝæÝ æááÇ áÇ
                for(int r=0 ; r<4 ; r++)
                {
                        f = 0;
                        color = arr[r][0];
                        if (color == '.') continue;
                        for(int c=0 ; c<4 ; c++)
                        {
                                if (arr[r][c] != color && arr[r][c] != 'T')
                                f = 1;  
                        }
                        if (f == 0)
                        {
                                wonrow[r] = 1;
                                break;
                        }
                }
                
                // ÚÔÇä ÇÔæÝ ÍÏ ÝÇÒ ÈÇáÃÚãÏÉ æááÇ áÇ
                for(int c=0 ; c<4 ; c++)
                {
                        f = 0;
                        color = arr[0][c];
                        if (color == '.') continue;
                        for(int r=0 ; r<4 ; r++)
                        {
                                if (arr[r][c] != color && arr[r][c] != 'T')
                                f = 1;  
                        }
                        if (f == 0)
                        {
                                wonclm[c] = 1;  
                                break;
                        }       
                }
                
                // ÝáÇÌ áæ ÍÏ ÝÇíÒ ÈÇáÕÝæÝ Çæ ÈÇáÃÚãÏÉ íäæÑ
                for(int i=0 ; i<4 ; i++)
                if (wonrow[i] == 1 || wonclm[i] == 1)
                { 
                        someonewin = 1;
                        break;
                }
                
                // ÚÔÇä ÇÔæÝ ÍÏ ÝÇÒ ÈÇáæÑÈ ãä ÇáÔãÇá ááíãíä æááÇ áÇ
                if (arr[0][0] != '.') 
                {
                        color = arr[0][0];
                        for(int r=0 , c=0 ; r<4 ; r++,c++)
                        {
                                if(arr[r][c] == color || arr[r][c] == 'T')
                                wrb[0] = 1;
                                else
                                {
                                        wrb[0] = 0;
                                        break;  
                                }
                        
                        }
                        wrbflag = 1;
                }
                
                // ÚÔÇä ÇÔæÝ ÍÏ ÝÇÒ ÈÇáæÑÈ ãä Çáíãíä ááÔãÇá æááÇ áÇ
                if (arr[0][3] != '.')
                {
                        color = arr[0][3];
                        for(int r=0 , c=3 ; r<4 ; r++,c--)
                        {
                                if(arr[r][c] == color || arr[r][c] == 'T')
                                wrb[1] = 1;
                                else
                                {
                                        wrb[1] = 0;
                                        break;  
                                }
                                        
                        }
                        wrbflag = 1;
                }
                
                // ÝáÇÌ áæ ÍÏ ÝÇÒ ÈÇáæÑÈ íäæÑ
                if(wrb[0] == 1 || wrb[1] == 1)
                someonewin = 1;
                
                for(int r=0 ; r<4 ; r++)
                {
                        for(int c=0 ; c<4 ; c++)
                        {
                                if (arr[r][c] == '.')
                                {
                                        therearepoints = 1;
                                        break;
                                }
                        }
                }
                
        //      cout << someonewin << ' ' << therearepoints << endl;
                
                if (!someonewin && therearepoints)
                {
                        cout << "Case #" << k << ":" << ' ' << "Game has not completed\n";
                        continue;
                }
                if (!someonewin && !therearepoints)
                {
                        cout << "Case #" << k << ":" << ' ' << "Draw\n";
                        continue;
                }
                
                char thewinner;
                bool flag = 0;
                if (someonewin)
                {
                        for(int i=0 ; i<4 ; i++)
                        {
                                if (wonrow[i] == 1)
                                {
                                        if (arr[i][0] != 'T') thewinner = arr[i][0];
                                        else thewinner = arr[i][1];
                                        
                                        cout << "Case #" << k << ":" << ' ' << thewinner << ' ' << "won\n";
                                        flag = 1;       
                                        break;
                                }
                        }
                        if (flag == 1) continue;
                        
                        for (int i=0 ; i<4 ; i++)
                        {
                                if (wonclm[i] == 1)
                                {
                                        if (arr[0][i] != 'T') thewinner = arr[0][i];
                                        else thewinner = arr[1][i];
                                        
                                        cout << "Case #" << k << ":" << ' ' << thewinner << ' ' << "won\n";
                                        flag = 1;
                                        break;
                                }
                        }
                        
                        if (flag == 1) continue;
                        
                        if (wrb[0])
                        {
                                if (arr[0][0] != 'T') thewinner = arr[0][0];
                                else thewinner = arr[1][1];
                                
                                cout << "Case #" << k << ":" << ' ' << thewinner << ' ' << "won\n";
                                flag = 1;       
                                
                        }
                        
                        if (flag == 1) continue;
                        
                        if (wrb[1])
                        {
                                if (arr[0][3] != 'T') thewinner = arr[0][3];
                                else thewinner = arr[1][2];
                                
                                cout << "Case #" << k << ":" << ' ' << thewinner << ' ' << "won\n";     
                        }
                        
                }
                
 
                
        }
        
 
        return 0;
}
 	
