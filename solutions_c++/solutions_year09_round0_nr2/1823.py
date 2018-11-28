#include <cstdio>
using namespace std;
int get_direction(int j,int height,int k,int weight,int (&alt)[100][100])
{
        int n,w,e,s,c;
        c = alt[j][k];
        int lowest = 0;
        int current = c;
        if(j == 0)
        { n = 10001;}
        else
        { n = alt[j-1][k];}

        if(j == (height - 1))
        { s = 10001;}
        else
        {s = alt[j+1][k];}

        if(k == 0)
        { w = 10001;}
        else
        { w = alt[j][k-1];}

        if(k == (weight - 1))
        { e = 10001;}
        else
        {e = alt[j][k+1];}

        if(current > n){current = n; lowest = 1;}
        if(current > w){current = w; lowest = 2;}
        if(current > e){current = e; lowest = 3;}
        if(current > s){current = s; lowest = 4;}
        return lowest;
}
int main(int argc, char* argv[])
{
        FILE *fp = fopen(*(argv+1), "r");
        int case_n, h, w;
        int alt[100][100];
        int dir[10000];
        int dir_count = 0;
        char basin[100][100];
        fscanf(fp, "%d", &case_n);
        for(int i = 0; i < case_n; i++)
        {
                fscanf(fp, "%d %d", &h, &w);
                for(int j = 0; j < h; j++)
                {
                        for(int k = 0; k < w; k++)
                        {
                                int temp_alt;
                                fscanf(fp, "%d", &temp_alt);
                                alt[j][k] = temp_alt;
                                basin[j][k] = '0';
                        }
                }
                char mark = 'a';
                char current_mark = 'a';
                bool inc_mark;
                for(int j = 0; j < h; j++)
                {
                        for(int k = 0; k < w; k++)
                        {
                                if(basin[j][k] == '0')
                                {
                                        dir_count = 0;
                                        int ver = j;
                                        int hor = k;
                                        inc_mark = true;
                                        mark = current_mark;
                                        int direction;
                                        while((direction = get_direction(ver,h,hor,w,alt)) != 0)
                                        {
                                                if(direction == 1) ver--;
                                                if(direction == 2) hor--;
                                                if(direction == 3) hor++;
                                                if(direction == 4) ver++;
                                                if(basin[ver][hor] != '0'){mark = basin[ver][hor];inc_mark = false;break;}
                                                dir[dir_count] = direction;
                                                dir_count++;
                                        }
                                        ver = j;
                                        hor = k;
                                        basin[ver][hor] = mark;
                                        for(int l = 0; l < dir_count; l++)
                                        {
                                                if(dir[l] == 1) ver--;
                                                if(dir[l] == 2) hor--;
                                                if(dir[l] == 3) hor++;
                                                if(dir[l] == 4) ver++;
                                                basin[ver][hor] = mark;
                                        }
                                        if(inc_mark == true)
                                        {
                                                current_mark++;
                                        }
                                }
                        }
                }
                printf("Case #%d:\n", i+1);
                for(int j = 0; j < h; j++)
                {
                        for(int k = 0; k < w; k++)
                        {
                                if(k != w -1)
                                {
                                        printf("%c ", basin[j][k]);
                                }
                                else
                                {
                                        printf("%c\n", basin[j][k]);
                                }
                        }
                }
        }
}