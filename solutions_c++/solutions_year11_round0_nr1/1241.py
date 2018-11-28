#include <stdio.h>

enum {

	BODY_O
	, BODY_B
	, BODY_TERM

};

int main(void)
{
	// ���E�����Ƃ��āA�n�_�� 1,1 �B
	// ���Ƃ͈ړ���̂���シ��Ƃ��͒��O�ɏ�������Ԃ��ė��p�ł���Ƃ����_�ɒ��ӁB

	// ��萔���擾
	int T = 0;
	scanf("%d",&T);

	// �����擾
	for(int round = 0;round < T;++round){

		// ��肪���V�[�P���X�̐�
		int N = 0;
		scanf("%d",&N);

		// OB �̈ʒu��������
		int pos[BODY_TERM] = {1,1,};

		// ��Ƃ�������
		int work = 0;

		// �c���Ă��鎞��
		int rem = 0;

		// ���O�̈ړ����
		int lastOB = BODY_TERM;

		// �����鎞��
		int totalTime = 0;
		
		// �V�[�P���X�̐��������[�v
		for(int seq = 0;seq < N;++seq){

			// ����̖���
			char rawBody;
			int targetPos;
			scanf(" %c %d",&rawBody,&targetPos);

			// ����̈ړ���̂� enum ��
			int body;
			switch( rawBody )
			{
			case 'O':
				body = BODY_O;
				break;
			default:
				body = BODY_B;
				break;
			}

			// ����̈ړ��Ƃۂ����ŏ���鎞�Ԃ͎�̕ω��ȂǊ֌W�Ȃ��v�Z�\

			// ����
			int time = targetPos - pos[body];
			if( time < 0 ) time = -time;

			// �ړ����܂��������
			pos[body] = targetPos;

			// �ړ���̂��؂�ւ�����璼�O�� work �� rem �Ɍv��ł���
			// ���̂Ƃ� rem �̓��Z�b�g�����
			if( lastOB != BODY_TERM && lastOB != body ){
				rem = work;
				work = 0;
			}

			// �c�莞�Ԃ̗��p
			if( time <= rem ){
				rem -= time;
				time = 0;
			}else{
				time -= rem;
				rem = 0;
			}

			// �{�^���ۂ����ɂ�铯��������̂Ŏc�莞�Ԃ͂P�񂵂��g���Ȃ�
			rem = 0;

			// �ۂ���
			++time;

			// ���܂�������Ȃ��������Ԃ��v��
			work += time;
			totalTime += time;

			// �ړ���̂��X�V
			lastOB = body;

		}

		// ���ʂ̕\��
		printf("Case #%d: %d\n",round+1,totalTime);

	}

	return 0;

}