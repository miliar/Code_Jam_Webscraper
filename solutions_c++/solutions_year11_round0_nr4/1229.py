#include <stdio.h>

int main(void)
{
	// ����u���������āA(�ʐ� - 1)x2 ���\�[�g�񐔊��Ғl�ɂȂ�

	int T = 0;
	scanf("%d",&T);

	int n[2000];
	int b[2000];

	for(int round = 0;round < T;++round){
		int N = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;++i){
			scanf("%d",&(n[i]));
			b[i] = 0;
		}

		// �܂����[�v���������Ă��Ȃ��ꏊ���珇�ɃT�[�`
		int totalRank = 0;
		int rank = 0;
		for(int i = 0;i < N;++i){

			if(b[i] == 0){

				// �����܂����T�[�`�ł��B
				// ���ꂩ�烋�[�v���`������Ă��邩���ׂ܂��B
				int start = i+1;
				int now = i+1;

				// now �� n[now-1] �ɒu������Ă���B
				// n[now-1] == start �Ȃ�I���B
				// ����Ă�����ʐ��𑝂₵�� n = n[now-1] �Ƃ��Ă������B
				rank = 1;
				while(n[now-1] != start){
					++rank;
					b[now-1] = 1;
					now = n[now-1];
				}
				b[now-1] = 1;

				totalRank += rank == 1 ? 0 : rank;//(rank - 1)*2;

			}

		}

		//for(int i = 0;i < N;++i){
		//	printf("%d",n[i]);
		//}printf("\n");

		printf("Case #%d: %d\n",round+1,totalRank);
	}

	return 0;
}