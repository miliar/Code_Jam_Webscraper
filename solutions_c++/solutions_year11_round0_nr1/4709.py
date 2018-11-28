#include <iostream>

int main(void)
{
	FILE* fp = fopen("A-large.in","r+");
	FILE* fp_2 = fopen("A-large.out","w+");

	int num_of_data;

	int orange[100][2];
	int blue[100][2];
	int orange_count, blue_count, all_count;

	fscanf(fp,"%d",&num_of_data);

	for(int i=0;i<num_of_data;++i)
	{
		int oper_num;

		fscanf(fp,"%d",&oper_num);

		orange_count = 0;
		blue_count = 0;
		all_count = 0;

		for(int j=0;j<oper_num;++j)
		{
			char OB;
			int button;

			fscanf(fp," %c %d",&OB,&button);

			all_count += 1;

			if(OB == 'O')
			{
				orange[orange_count][0] = button;
				orange[orange_count][1] = all_count;
				orange_count += 1;
			}
			else
			{
				blue[blue_count][0] = button;
				blue[blue_count][1] = all_count;
				blue_count += 1;
			}
		}

		int step = 1;
		int all_do_count = 1;
		int orange_do_count = 0;
		int blue_do_count = 0;
		int orange_site = 1;
		int blue_site = 1;

		while(1)
		{
			bool orange_move = false;
			bool blue_move = false;

			if((orange_do_count < orange_count) && (orange_site < orange[orange_do_count][0]))
			{
				orange_move = true;
				orange_site += 1;
			}
			else if((orange_do_count < orange_count) && (orange_site > orange[orange_do_count][0]))
			{
				orange_move = true;
				orange_site -= 1;
			}

			if((blue_do_count < blue_count) && (blue_site < blue[blue_do_count][0]))
			{
				blue_move = true;
				blue_site += 1;
			}
			else if((blue_do_count < blue_count) && (blue_site > blue[blue_do_count][0]))
			{
				blue_move = true;
				blue_site -= 1;
			}

			bool did = false;

			if((orange_do_count < orange_count) && (!orange_move) && (orange[orange_do_count][0] == orange_site) && (orange[orange_do_count][1] == all_do_count))
			{
				orange_do_count += 1;
				did = true;
			}
			else if((blue_do_count < blue_count) && (!blue_move) && (blue[blue_do_count][0] == blue_site) && (blue[blue_do_count][1] == all_do_count))
			{
				blue_do_count += 1;
				did = true;
			}

			if(did)
				all_do_count += 1;

			if((orange_do_count == orange_count) && (blue_do_count == blue_count))
				break;

			step += 1;
		}

		printf("Case #%d: %d\n",i+1,step);
		fprintf(fp_2,"Case #%d: %d\n",i+1,step);
	}

	fclose(fp);

	return 0;
}

/*
상태 : 버튼 누르기, 이동, 기다리기
*/