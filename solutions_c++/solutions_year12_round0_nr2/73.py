#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d\n",&T);
    for(int r = 0;r < T;++r){
        printf("Case #%d: ", r+1);
        int N,S,P;
        scanf("%d %d %d ", &N, &S, &P);
        int ans = 0;
        for(int i = 0;i < N;++i){
            int total;
            scanf("%d",&total);
            // �f�_�ŕ���
            int rawscore = (total+2)/3;
            int mod = total % 3;
            if( rawscore >= P ){
                // ���i
                ++ans;
            }else if( rawscore >= P - 1 ){
                // �ɂ����B
                // ���_���ړ��\�ŁA���T�v���C�W���O�g���c���Ă�΂���ŏ��i�B
                if( total > 1 && (mod == 0 || mod == 2) && S ){
                    ++ans;
                    --S;
                }
            }
        }
        printf("%d\n",ans);
    }
}