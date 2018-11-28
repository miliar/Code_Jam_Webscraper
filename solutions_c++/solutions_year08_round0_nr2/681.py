#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#define MAX 450
using namespace std;
struct train {
       int s;
       int e;
};
train a[101];
train b[101];
int t;
int na, nb;
char st[50];
char en[50];
bool vc[MAX][MAX];
int resa, resb;
int q[MAX], prev[MAX], qs, qe; 
    //q��BFS�õĶ��У�prev��������¼�������ģ�ͬʱҲ������¼�ұߵĵ��Ƿ��ҹ�
int vm1[MAX], vm2[MAX]; 
inline int timetoint(char *str) {
    return ((int)(str[0] - '0')) * 10 * 60 + (str[1] - '0') * 60 + (str[3] - '0') * 10 + str[4] - '0';
}
//�������㷨ʵ�� vc from 0 to MAX
int Bipartite(bool vc [][MAX],int nv1,int nv2) { 
    //vc[][]Ϊ����ͼ��nv1,nv2�ֱ�Ϊ��ߵĵ��� 
    int i, j, x, n; 
    //nΪ���ƥ���� 
    
    //vm1,vm2�ֱ��ʾ���ߵĵ�����һ�ߵ��ĸ�����ƥ�� 
    n = 0; 
    for( i = 0; i < nv1; i++ ) vm1[i] = -1; 
    for( i = 0; i < nv2; i++ ) vm2[i] = -1; //��ʼ�����е�Ϊδ��ƥ���״̬
    for( i = 0; i < nv1; i++ ) { 
        if(vm1[i] != -1)continue;
        //�������ÿһ��δ��ƥ��ĵ����һ��BFS�ҽ����� 
        
        for( j = 0; j < nv2; j++ ) prev[j] = -2; 
        //ÿ��BFSʱ��ʼ���ұߵĵ�
         
        qs = qe = 0; //��ʼ��BFS�Ķ��� 
        //�����ⲿ�ִ���ӳ�ʼ���Ǹ��㿪ʼ���Ȱ������ҵĵ��ұߵĵ�������
        //����΢��һ�¿������������ڽӱ�ʵ�ֵĶ���ͼ 
        for( j = 0; j < nv2; j++ ) if( vc[i][j] ) { 
            prev[j] = -1; 
            q[qe++] = j; 
        } 
         
        while( qs < qe ) { //BFS
            x = q[qs]; 
            if( vm2[x] == -1 ) break; 
            //����ҵ�һ��δ��ƥ��ĵ㣬��������ҵ���һ�������� 
            qs++; 
            //�����ⲿ������չ���Ĵ��룬����΢��һ�¿������������ڽӱ�ʵ�ֵĶ���ͼ 
            for( j = 0; j < nv2; j++ ) if( prev[j] == -2 && vc[vm2[x]][j] ) { 
                //������ұߵ���һ���Ѿ���ƥ��ĵ㣬��vm2[x]����õ���ƥ�����ߵ� 
                //�Ӹ���ߵ������Ѱ�����������ҵ����ұߵ� 
                prev[j] = x; 
                q[qe++] = j; 
            } 
        } 
        if( qs == qe ) continue; //û���ҵ������� 
        
        //���Ľ�������ƥ��״̬ 
        while( prev[x] > -1 ) { 
            vm1[vm2[prev[x]]] = x; 
            vm2[x] = vm2[prev[x]]; 
            x = prev[x]; 
        } 
        vm2[x] = i; 
        vm1[i] = x; 
        
        //ƥ��ı�����һ 
        n++; 
    } 
    return n; 
} 
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while (T--) {
           scanf("%d", &t);
           scanf("%d %d", &na, &nb);
           getchar();
           memset(vc,0, sizeof(vc));
           for (int i = 0; i < na; i++) {
                scanf("%s %s", st, en);
                getchar();
                a[i].s = timetoint(st);
                a[i].e = timetoint(en);
           }
           for (int i = 0; i < nb; i++) {
                scanf("%s %s", st, en);
                getchar();
                b[i].s = timetoint(st);
                b[i].e = timetoint(en);
           }
           for (int i = 0; i < na; i++)
                for (int j = 0; j < nb; j++) {
                     if (a[i].e + t <= b[j].s) {
                         vc[i][na + j] = 1;
                     }
                     if (b[j].e + t <= a[i].s) {
                         vc[na + j][i] = 1;
                     }
                }
           Bipartite(vc, na + nb, na + nb);
           resa = 0;
           resb = 0;
           /*
           for (int i = 0; i < na + nb; i++)
           {
                printf("vm1[%d]=%d\n", i, vm1[i]);
                printf("vm2[%d]=%d\n", i, vm2[i]);
           }
           */
           for (int i = 0; i < na + nb; i++) {
                bool flag = false;
                if (vm2[i] != -1)
                    continue;
                if (!flag) {
                    //printf("%d\n", i);
                    if (i < na)
                        resa++;
                    else
                        resb++;
                }
           }
           printf("Case #%d: %d %d\n", ++cnt, resa, resb);
    }
}
