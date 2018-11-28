/*#include <iostream>
#include <fstream>
#include <ctime>
using namespace std;

#define n 100
#define m 45000

int main(){
	int i,q,x,y;
	srand(time(0));
	ofstream fout("Êý¾Ýin.txt",ios::out);
	fout<<n<<' '<<m<<endl;
	for(i=0;i<m;i++){
		q=rand()%2;
		if(q==1){
			fout<<"C ";
			x=rand()%n+1;
			y=rand()%n+1;
			fout<<rand()%x+1<<' '<<rand()%y+1<<' '<<x<<' '<<y<<endl;
		}
		else{
			fout<<"Q ";
			fout<<rand()%n+1<<' '<<rand()%n+1<<endl;
		}
	}
	return 0;
}
*/

//#include <iostream>
//#include <fstream>
//#include <ctime>
//using namespace std;
//
//int main(){
//	srand(time(0));
//	ofstream fout("in.txt",ios::out);
//	int i, j, l, r, T = 10, x, v, t;
//	while (T--){
//		x = v = 0;
//
//		fout << 5 << ' ';
//		int n = 5;
//		fout << n << endl;
//		for (i = 0; i < 5; i++)
//			fout << rand() % 5 << ' ';
//		fout << endl;
//		for (i = 1; i <= n; i++){
//			if (rand() & 1){
//				fout << "Q ";
//				r = rand() % 5 + 1;
//				l = rand() % r + 1;
//				fout << l << ' ' << r << endl;
//			}
//			else{
//				fout << "C ";
//				r = rand() % 5 + 1;
//				l = rand() % r + 1;
//				t = rand() % 10;
//				fout << l << ' ' << r << " " << t << endl;
//			}
//		}
//		fout << endl;
//	}
//	return 0;
//}

//#include<iostream>
//#include<queue>
//using namespace std;
//struct node
//{
//    long f;
//    long next[27];
//    long fall;
//    void init(){memset(next,-1,sizeof(next));fall=f=0;}
//}s[2000000];
//long p;
//char a[1000005];
//void preprocess(){s[p=0].init();s[0].fall=-1;}
//
//void insert()
//{
//    long index=0;
//    long i;
//    for(i=0;a[i];++i)
//    {
//        int x=a[i]-'a';
//        if(s[index].next[x]==-1)
//        {
//            s[++p].init();
//            s[index].next[x]=p;
//        }
//        index=s[index].next[x];
//    }
//    ++s[index].f;
//}
//
//long find()
//{
//    long index=0;
//    long root=0;
//    long i;
//     long ct=0;
//    long father=root;
//    for(i=0;a[i];)
//    {    
//        long x=a[i]-'a';
//        index=s[father].next[x];
//
//        if(index!=-1)
//        {
//            if (s[index].f)
//            {
//                ct+=s[index].f;
//                s[index].f=0;
//            }
//            father=index;    
//            ++i;        
//        }
//        else
//        {    
//            while(father!=-1&&s[father].next[x]==-1)
//            {    
//                father=s[father].fall;    
//                if (father!=-1&&s[father].f)
//                {
//                    ct+=s[father].f;
//                    s[father].f=0;
//                    
//                }                
//            }
//
//            if (father==-1)
//            {
//                father=root;
//                ++i;
//            }
//        }
//
//    }
//    return ct;
//    
//}
//
//
//void KMP()
//{
//    long root=0;
//    queue<long> q;
//    q.push(root);
//    while (!q.empty())
//    {
//        long t=q.front();
//        q.pop();
//
//        long i;
//        for (i=0;i<26;++i)
//        {
//            long index=s[t].next[i];
//            if(index!=-1)
//            {
//                long father=s[t].fall;
//                while (father!=-1&&s[father].next[i]==-1)
//                {
//                    father=s[father].fall;
//                }
//
//                if(father!=-1)
//                {
//                    s[index].fall=s[father].next[i];
//                }
//                else
//                {
//                    s[index].fall=0;
//                }
//                q.push(index);
//            }
//        }
//    }
//}
//
//
//int main()
//{
//
//    long T;
//    scanf("%ld",&T);
//    
//    while(T--)
//    {
//        preprocess();
//        long n;
//        scanf("%ld",&n);
//        getchar();
//        while (n--)
//        {
//            gets(a);
//            insert();
//        }
//        gets(a);
//        char x[2];
//        x[0]='z'+1;
//        x[1]='\0';
//        strcat(a,x);
//        KMP();
//        printf("%ld\n",find());
//    }
//
//    return 0;
//}







//Program happybirthday;
//Uses
//  happybirthday_p;
//Const
//  MaxNode       =1000000;
//Type
//  TreeType      =Record
//    Left,Right  :LongInt;
//    Count,Father:LongInt;
//  End;
//  ListType      =Record
//    Num,Next    :LongInt;
//  End;
//Var
//  Sons          :Array[0..MaxNode,1..2] Of LongInt;
//  Father,Count  :Array[0..MaxNode] Of LongInt;
//  Data1,Data2   :Array[0..MaxNode] Of LongInt;
//  List          :Array[0..MaxNode] Of ListType;
//  Root          :LongInt;
//  TotalTreeNode :LongInt;
//  TotalListNode :LongInt;       
//Procedure Rotate(X,W:LongInt);
//Var
//  Y             :LongInt;
//Begin
//  Y := Father[X];
//  Count[Y] := Count[Y] - Count[X] + Count[Sons[X,W]];
//  Count[X] := Count[X] - Count[Sons[X,W]] + Count[Y];
//  Sons[Y,3-W] := Sons[X,W];
//  If Sons[X,W]<>0 Then Father[Sons[X,W]] := Y;
//  Father[X] := Father[Y];
//  If Father[Y]<>0 Then
//    If Y=Sons[Father[Y],1]
//      Then Sons[Father[Y],1] := X Else Sons[Father[Y],2] := X;
//  Father[Y] := X;  Sons[X,W] := Y;
//End;
//
//
//
//Procedure Splay(X:LongInt);
//Var
//  Y:LongInt;
//Begin
//  While Father[X]<>0 Do Begin
//    Y := Father[X];
//    If Father[Y]=0 Then
//      If X=Sons[Y,1] Then Rotate(X,2) Else Rotate(X,1)
//    Else
//      If Y=Sons[Father[Y],1]
//        Then
//          If X=Sons[Y,1]
//            Then Begin  Rotate(Y,2);  Rotate(X,2);  End
//            Else Begin  Rotate(X,1);  Rotate(X,2);  End
//        Else
//          If X=Sons[Y,2]
//            Then Begin  Rotate(Y,1);  Rotate(X,1);  End
//            Else Begin  Rotate(X,2);  Rotate(X,1);  End;
//  End;
//  Root := X;
//End;
//
//
//
//Function Search(X,W:LongInt):LongInt;
//Begin
//  While Data1[X]<>W Do Begin
//    If W<=Data1[X] Then Begin
//      If Sons[X,1]=0 Then Break;
//      X := Sons[X,1];
//    End
//    Else Begin
//      If Sons[X,2]=0 Then Break;
//      X := Sons[X,2];
//    End
//  End;
//  Search := X;
//End;
//
//
//
//Procedure Insert(U,V:LongInt);
//Var
//  Y             :LongInt;
//Begin
//  If TotalTreeNode=0 Then Begin
//    Inc(TotalTreeNode);  Inc(TotalListNode);
//    Data1[1] := U;  Data2[1] := 1;  List[1].Num := V;  Count[1] := 1;
//    Root := 1;
//    Exit;
//  End;
//  Y := Search(Root,U);
//  If Data1[Y]<>U Then Begin
//    Inc(TotalTreeNode);
//    Data1[TotalTreeNode] := U;
//    Father[TotalTreeNode] := Y;
//    If U<Data1[Y] Then Sons[Y,1] := TotalTreeNode Else Sons[Y,2] := TotalTreeNode;
//    If U<Data1[Y] Then Y := Sons[Y,1] Else Y := Sons[Y,2];
//  End;
//  Splay(Y);
//  Inc(Count[Root]);
//  If Data2[Root]=0 Then Begin
//    Inc(TotalListNode);
//    List[TotalListNode].Num := V;
//    Data2[Root] := TotalListNode;
//  End
//  Else Begin
//    Y := Data2[Root];
//    While List[Y].Next<>0 Do Y := List[Y].Next;
//    Inc(TotalListNode);
//    List[Y].Next := TotalListNode;
//    List[TotalListNode].Num := V;
//  End;
//End;
//
//
//
//
//
//Procedure Delete(T:LongInt;Var U,V:LongInt);
//Var
//  Y             :LongInt;
//Begin
//  Y := Root;
//  Repeat
//    If T<=Count[Sons[Y,1]] Then Y := Sons[Y,1]
//      Else If T>Count[Y]-Count[Sons[Y,2]] Then Begin
//        T := T - Count[Y]+Count[Sons[Y,2]];
//        Y := Sons[Y,2];
//      End Else Break;
//  Until False;
//  U := Data1[Y];  V := List[Data2[Y]].Num;
//  Splay(Y);
//  Dec(Count[Root]);
//  Data2[Root] := List[Data2[Y]].Next;
//End;
//
//
//
//Procedure Main;
//Var
//  I,Kth,T1,T2   :LongInt;
//  IsBoy,IsEnd   :Boolean;
//Begin
//  I := 0;
//  Repeat
//    Inc(I);
//    IsEnd := getpresent(T1,T2,IsBoy);
//    If IsEnd=False Then Break;
//    Insert(T1,I);
//    Kth := Count[Sons[Root,1]] + 1;
//    If IsBoy Then Kth := Kth + T2 Else Kth := Kth - T2;
//    If (Kth<1) Or (Count[Root]<Kth) Then Tell(-1)
//    Else Begin
//      Delete(Kth,T1,T2);
//      If T1>0 Then Begin
//        Tell(T2); 
//        Insert(T1-1,T2);
//      End Else Tell(-1);
//    End;
//  Until False;
//End;
//Begin  {Main}
//  Init;
//  Main;
//End.

//#include <iostream>
//using namespace std;
//
//int main(){
//	int i, j, k, s, cnt = 0;
//	int ii, jj, kk, ss;
//	for (i = 0; i < 1000; i++){
//		j = i + 1, k = j + 1;
//		s = i + j + k;
//		ii = i, jj = j, kk = k, ss = s;
//		while (kk){
//			if (ii % 10 + jj % 10 + kk % 10 != ss % 10)
//				break;
//			ii /= 10, jj /= 10, kk /= 10, ss /= 10;
//		}
//		if (ii == 0){
//			printf("%d %d %d\n", i, j, k);
//			cnt++;
//		}
//	}
//	printf("%d\n", cnt);
//	while(1);
//	return 0;
//}


//#include <iostream>
//using namespace std;
//
//short g[20010][20010];
//char str[10010];
//
//int mov[4][2] = {
//	{-1, 0},
//	{1, 0},
//	{0, -1},
//	{0, 1}
//};
//int ll[4] = {2, 3, 1, 0};
//int rr[4] = {3, 2, 0, 1};
//char op[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
//
//int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
//	int i, j, k, T;
//	int l, r, u, d;
//	int len;
//	int dir;
//	int cas = 1;
//	scanf("%d", &T);
//	getchar();
//	while (T--){
//		l = 201, r = 0, u = 201, d = 0;
//		memset(g, 0, sizeof(g));
//		scanf("%s", str);
//		len = strlen(str);
//		l = r = u = d = i = j = 10001;
//		dir = 1;
//		for (k = 1; k < len; k++){
// 			if (k && k < len - 1){
//				if (j < l)l = j;
//				if (j > r)r = j;
//				if (i < u)u = i;
//				if (i > d)d = i;
//			}
//
//			if (str[k] == 'L')
//				g[i][j] |= (1 << ll[dir]);
//			else if (str[k] == 'W')
//				g[i][j] |= (1 << dir);
//			else if (k < len - 1 && str[k + 1] != 'R')
//				g[i][j] |= (1 << rr[dir]);
//
//			if (str[k] == 'R')
//				dir = rr[dir];
//			else if (str[k] == 'L')
//				dir = ll[dir];
//			else{
//				i += mov[dir][0];
//				j += mov[dir][1];
//			}
//		}
//
//		scanf("%s", str);
//		len = strlen(str);
//		dir = rr[rr[dir]];
//		for (k = 0; k < len; k++){
// 			if (k && k < len - 1){
//				if (j < l)l = j;
//				if (j > r)r = j;
//				if (i < u)u = i;
//				if (i > d)d = i;
//			}
//
//			if (str[k] == 'L')
//				g[i][j] |= (1 << ll[dir]);
//			else if (str[k] == 'W')
//				g[i][j] |= (1 << dir);
//			else if (k < len - 1 && str[k + 1] != 'R')
//				g[i][j] |= (1 << rr[dir]);
//
//			if (str[k] == 'R')
//				dir = rr[dir];
//			else if (str[k] == 'L')
//				dir = ll[dir];
//			else{
//				i += mov[dir][0];
//				j += mov[dir][1];
//			}
//		}
//		printf("Case #%d:\n", cas++);
//		for (i = u; i <= d; i++){
//			for (j = l; j <= r; j++){
//				printf("%c", op[g[i][j]]);
//			}
//			printf("\n");
//		}
//	}
//	return 0;
//}


//#include <iostream>
//using namespace std;
//
//#define MAX 100000
//
//int child[MAX][26];
//int ncnt;
//
//int len, n, m;
//int ans;
//
//char str[1000];
//
//void insert(char *str){
//	int i, c, p = 0;
//	while (*str){
//		c = *str - 'a';
//		if (child[p][c] == -1){
//			ncnt++;
//			child[p][c] = ncnt;
//		}
//		p = child[p][c];
//		str++;
//	}
//}
//
//int d[20][26], cnt[20];
//
//void dfs(int k, int p){
//	int i, j;
//	if (k == len){
//		ans++;
//		return;
//	}
//	for (i = 0; i < cnt[k]; i++){
//		j = d[k][i];
//		if (child[p][j] != -1){
//			dfs(k + 1, child[p][j]);
//		}
//	}
//}
//
//
//
//int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
//	int i, j, k, l, cas;
//	while (scanf("%d %d %d", &len, &n, &m) != EOF){
//		cas = 1;
//		getchar();
//		memset(child, -1, sizeof(child));
//		ncnt = 0;
//		for (i = 0; i < n; i++){
//			scanf("%s", str);
//			insert(str);
//		}
//		for (i = 1; i <= m; i++){
//			memset(cnt, 0, sizeof(cnt));
//			scanf("%s", str);
//			l = strlen(str);
//			j = k = 0;
//			while (j < l){
//				if (str[j] == '('){
//					j++;
//					while (str[j] != ')'){
//						d[k][cnt[k]++] = str[j] - 'a';
//						j++;
//					}
//					j++;
//				}
//				else{
//					d[k][cnt[k]++] = str[j] - 'a';
//					j++;
//				}
//				k++;
//			}
//			printf("Case #%d: ", cas++);
//			if (k != len){
//				printf("0\n");
//				continue;
//			}
//			ans = 0;
//			dfs(0, 0);
//			printf("%d\n", ans);
//		}
//	}
//	return 0;
//}



#include <iostream>
using namespace std;

int g[110][110], n, m;
int a[110][110];

int mov[4][2] = {
	{-1, 0},
	{0, -1},
	{0, 1},
	{1, 0}
};

int cx, cy;

void chose(int x, int y){
	cx = -1, cy = -1;
	int i, nx, ny;
	for (i = 0; i < 4; i++){
		nx = x + mov[i][0];
		ny = y + mov[i][1];
		if (0 <= nx && nx < n && 0 <= ny && ny < m && ((cx == -1 || g[nx][ny] < g[cx][cy]) && g[nx][ny] < g[x][y])){
			cx = nx, cy = ny;
		}
	}
}


void dfs(int x, int y, int tag, bool bj){
	int i, nx, ny, mnx = -1, mny = -1;
	a[x][y] = tag;
	chose(x, y);
	if (cx != -1 && !bj){
		if (a[cx][cy] == -1){
			dfs(cx, cy, tag, false);
		}
	}
	for (i = 0; i < 4; i++){
		nx = x + mov[i][0];
		ny = y + mov[i][1];
		if (0 <= nx && nx < n && 0 <= ny && ny < m && a[nx][ny] == -1 && g[nx][ny] > g[x][y]){
			chose(nx, ny);
			if (cx == x && cy == y)
				dfs(nx, ny, tag, true);
		}
	}
}



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cnt;
	int i, j;
	int T, cas = 1;
	scanf("%d", &T);
	while (T--){
		cnt = 0;
		memset(a, -1, sizeof(a));
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; i++){
			for (j = 0; j < m; j++){
				scanf("%d", &g[i][j]);
			}
		}
		for (i = 0; i < n; i++){
			for (j = 0; j < m; j++){
				if (a[i][j] == -1){
					dfs(i, j, cnt, false);
					cnt++;
				}
			}
		}
		printf("Case #%d:\n", cas++);
		for (i = 0; i < n; i++){
			printf("%c", a[i][0] + 'a');
			for (j = 1; j < m; j++){
				printf(" %c", a[i][j] + 'a');
			}
			printf("\n");
		}
	}
	return 0;
}


//#include<iostream>
//using namespace std;
//
//const int MAX = 110;
//const int mov[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
//
//int water[MAX][MAX];
//int mark[MAX][MAX];
//int cnt;
//int h, w;
//
//void Init()
//{
//	scanf("%d%d", &h, &w);
//	memset(water, 0x5e, sizeof(water));
//	memset(mark, -1, sizeof(mark));
//	int i, j;
//	for(i=1; i<=h; ++i)
//	{
//		for(j=1; j<=w; ++j)
//			scanf("%d", &water[i][j]);
//	}
//	cnt = 0;
//}
//
//void dfs(int x, int y)
//{
//	int i, dir = -1, mn = water[x][y], xx, yy;
//	for(i=0; i<4; ++i)
//	{
//		xx = x + mov[i][0]; yy = y + mov[i][1];
//		if(water[xx][yy] < mn)
//		{
//			dir = i;
//			mn = water[xx][yy];
//		}
//	}
//	if(dir == -1)mark[x][y] = cnt++;
//	else 
//	{
//		xx = x + mov[dir][0];
//		yy = y + mov[dir][1];
//		if(mark[xx][yy] < 0)dfs(xx, yy);
//		mark[x][y] = mark[xx][yy];
//	}
//}
//
//void Solve(int no)
//{
//	int i, j;
//	for(i=1; i<=h; ++i)
//	{
//		for(j=1; j<=w; ++j)
//		{
//			if(mark[i][j] < 0)dfs(i, j);
//		}
//	}
//	printf("Case #%d:\n", no);
//	for(i=1; i<=h; ++i)
//	{
//		for(j=1; j<=w; ++j)
//		{
//			if(j != 1)putchar(' ');
//			putchar('a'+mark[i][j]);
//		}
//		putchar('\n');
//	}
//}
//
//int main()
//{
//	int n, i;
//	scanf("%d", &n);
//	for(i=1; i<=n; ++i)
//	{
//		Init();
//		Solve(i);
//	}
//	return 0;
//}


//#include <iostream>
//#include <stack>
//using namespace std;
//
//char str[1000000010], s1[209], s2[200];
//int l, l1, l2;
//
//stack<char> st;
//
//int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
//
//	int i, j, T, t, tt;
//	int cas = 1;
//	scanf("%d", &T);
//	getchar();
//	while (T--){
//		printf("Case #%d: ", cas++);
//		scanf("%s %s %s", str, s1, s2);
//		l = strlen(str);
//		l1 = strlen(s1);
//		l2 = strlen(s2);
//
//		t = 0;
//		for (i = 0; i < l; i++){
//			for (j = 0; j < l1; j++)
//				if (str[i] == s1[j])
//					break;
//			t = t * l1 + j;
//		}
//
//		while (t){
//			tt = t % l2;
//			t /= l2;
//			st.push(s2[tt]);
//		}
//		while (!st.empty()){
//			printf("%c", st.top());
//			st.pop();
//		}
//		printf("\n");
//	}
//	return 0;
//}




