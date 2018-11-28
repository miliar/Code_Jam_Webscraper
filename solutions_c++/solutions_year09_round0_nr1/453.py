#include<cstdio>
#include<cstring>

const int M = 160000;

struct node 
{
    int next[26];
    int val;
};

node mem[M];
int top, L, N, D, ans;

int Get_val(char ch){
    return ch - 'a';
}

void Add_str(char a[], int val)
{
    int i, cur = 0;
    for(i = 0; a[i] != '\0'; i ++)
    {
        if(mem[cur].next[Get_val(a[i])] == 0)
        {
            mem[cur].next[Get_val(a[i])] = top;
            cur = top++;
        }
        else {
            cur = mem[cur].next[Get_val(a[i])];
        }
    }
    mem[cur].val = val;
}

void Find_str(char a[], int s[], int e[], int d, int cur)
{
	int i;
    if(d < L){
		for(i = s[d]; i <= e[d]; i ++)
		{
			if(mem[cur].next[Get_val(a[i])] != 0)
			{
				Find_str(a, s, e, d+1, mem[cur].next[Get_val(a[i])]);
			}
		}
	}
    else {
		ans += mem[cur].val;
	}
}

void init()
{
    memset(mem, 0, top*(sizeof(node)));
    top = 1;
}

int main()
{
    int i, j, n, m, val, cc = 0;
    int start[10000], end[10000], cnt;
    char tmp[40], s[10010];

    scanf("%d %d %d", &L, &D, &N);
	init();
    for(i = 0; i < D; i ++)
    {
        scanf("%s", tmp);
        Add_str(tmp, 1);
    }
    for(i = 0; i < N; i ++)
    {
		scanf("%s", s);
		ans = 0;
		cnt = 0;
		bool flag = false;
		for(j = 0; s[j] != '\0'; j ++)
		{
			if(flag){
				if(s[j] == ')'){
					flag = false;
					end[cnt] = j-1;
					cnt ++;
				}
			}
			else {
				if(s[j] == '('){
					start[cnt] = j+1;
					flag = true;
				}
				else {
					start[cnt] = end[cnt] = j;
					cnt ++;
				}
			}
		}
		Find_str(s, start, end, 0, 0);
		printf("Case #%d: %d\n", ++cc, ans);
	}
    return 0;
}

