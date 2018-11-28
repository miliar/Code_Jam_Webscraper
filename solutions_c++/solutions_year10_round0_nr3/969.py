#include <stdio.h>
#include <queue>

using namespace std;

typedef unsigned int u32;
typedef unsigned long long u64;

int main(void){

	FILE* fp = 0;
	FILE* out = 0;
	fp = fopen("prob.txt","rb");
	out = fopen("out.txt","wb");

	u32 maxRound = 0;

	fscanf( fp, "%u\n", &maxRound );
	//printf("%u\n",maxRound);

	for(u32 i = 0;i < maxRound;++i){

		// R k N ��ǂݎ��
		u32 runTimes = 0;
		u32 maxSeat = 0;
		u32 groupMax = 0;
		fscanf( fp, "%u %u %u\n", &runTimes, &maxSeat, &groupMax );

		// �҂��l�Ə���Ă�l
		queue<u32> waitQueue;
		queue<u32> riderQueue;

		// �O���[�v��ǂݎ��
		for(u32 z = 0;z < groupMax;++z){
			u32 group = 0;
			fscanf(fp,"%u",&group);
			waitQueue.push( group );
		}

		// ��߂Ă�[�B
		// �ł̓R�[�X�^�[�ɏ悹���邾���悹�āA
		// ���点�āA���ǂ��A���Ă̂��c�Ɖ񐔂����J��Ԃ��B
		u32 earn = 0;
		for(u32 k = 0;k < runTimes;++k){

			// waitQueue ���� maxSeat �̌��E�܂ň�������o��
			u32 currentSeat = 0;
			while( waitQueue.empty() == false ){

				// ���̃O���[�v��˂����񂾂Ƃ��āA
				// �V�[�g�������z���邩�z���Ȃ����H
				if( currentSeat + waitQueue.front() <= maxSeat ){

					// �Z�[�t�B������Ă��܂����B
					currentSeat += waitQueue.front();
					riderQueue.push( waitQueue.front() );
					waitQueue.pop();

				}else{

					// ����A�������Ȃ��B
					// ������B
					break;

				}

			}

			// �V�[�g�Ɍ��E�܂ŏ�����悤���B
			// ���点�āA��������I
			earn += currentSeat;

			// ��ŁA�Ăя��҂��L���[�ɏ������
			while( riderQueue.empty() == false ){
				waitQueue.push( riderQueue.front() );
				riderQueue.pop();
			}
		}

		// �҂��̕\��
		fprintf(out,"Case #%u: %u\n",i+1,earn);

	}

	fclose(fp);
	fclose(out);
}