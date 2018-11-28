#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <math.h>

const double EPS = 1.0e-6;

struct Car
{ double t; double x; };

double D;
Car c[3000];
double g[500];

void solve(int cn, int gid)
{
    // 1/2 a (t - ts)^2 �̃��C����
    // ts > 0 �ő�������ׂĈ��ݍ��ނ��A�ڂ���悤�� ts ��T���A
    // ���Ƃ͂��� ts ����ő��ō~������΂悢�B
    // ���肪�S�[�����鎞�Ԃ𒲂ׂ�
    double t = 0;
    for(int i = 0;i < cn;++i){
        if( c[i].x >= D ){
            // �S�[�������B
            // �ڍׂȎ��Ԃ��o��
            if( i <= 0 ){
                // �ŏ�����S�[�����Ă�
                t = 0;
                c[0].t = 0;
                c[0].x = D;
                cn = 1;
            }else{
                // ��O�̒n�_���炱�̒n�_�܂ł̋�ԂŃS�[�����Ă�
                double rem = D - c[i-1].x;
                double speed = (c[i].x - c[i-1].x)/(c[i].t - c[i-1].t);
                t = c[i-1].t + rem / speed;
                c[i].t = t;
                c[i].x = D;
                cn = i+1;
            }
            break;
        }
    }

    // (0,0) ����J�n���āA�ec�_��ʂ� ts ���v�Z���A
    // �ŏ��ɂ��ׂĂ� c �_��ʉ߂ł����������̗p����

    for(int i = -1;i < cn;++i){
        Car dc;
        if( i < 0 ){
            dc.t = 0;
            dc.x = 0;
        }else{
            dc = c[i];
        }

        // dc ��ʂ邽�߂� ts �͂����H
        double ts = dc.t - sqrt(2*dc.x/g[gid]);

        // �ߋ��ɂ����̂ڂ�Ȃ���΂Ȃ�Ȃ��悤�Ȃ���p
        if( ts < 0 - EPS ) continue;

        // cn ����� c �_�����ׂĉ���ł���Ȃ炱����̗p
        bool cleared = true;
        for(int z = i+1;z < cn;++z){
            // �����֎��������_�ł̈ʒu���A���̓_�𒴂��ĂȂ����OK�B
            // �����Ă���A�E�g�B
            double p = 0.5 * g[gid] * (c[z].t - ts) * (c[z].t - ts);
            if( p > c[z].x ){
                cleared = false;
                break;
            }
        }

        // �̗p����Ă��炻�ꂪ�����ƂȂ�p�X
        if( cleared ){
            // �����鎞�Ԃ� ts + sqrt(2D/g)
            printf("%.6f\n",ts + sqrt(2 * D / g[gid]));
            break;
        }
    }

}

int main(void)
{
    int T;
    scanf("%d\n",&T);
    for(int r = 0;r < T;++r){
        printf("Case #%d: ", r+1);
        printf("\n");
        // ���肪�S�[�����鎞�Ԃ��ƂĂ��厖
        int N;
        int A;
        scanf("%lf %d %d\n",&D,&N,&A);
        //printf("\n%.6f %d %d\n",D,N,A);
        for(int n = 0;n < N;++n){
            scanf("%lf %lf\n",&(c[n].t),&(c[n].x));
            //printf("%.6f %.6f\n",c[n].t,c[n].x);
        }
        for(int a = 0;a < A;++a){
            scanf("%lf",&g[a]);
            //printf("%.6f ",g[a]);
            solve(N,a);
        }
    }
    return 0;
}