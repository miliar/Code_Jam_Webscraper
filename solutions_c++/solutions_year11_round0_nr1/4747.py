//============================================================================
// Name        : BotTrust.cpp
// Author      : TOKUMOTO Susumu
// Version     :
// Copyright   :
// Description :
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define DPRINT printf
#define DPRINT

int main(int argc, char *argv[]) {
	int ret = EXIT_SUCCESS;
	char buf[1000];
	FILE *fp = NULL;
	long t, n, i;
	char *tmpptr = NULL;

	memset(buf, 0, sizeof(buf));
	if(argc < 1){
		printf("argument error\n");
		return EXIT_FAILURE;
	}
	fp = fopen(argv[1], "r");
	if(fp == NULL){
		printf("filename error\n");
		return EXIT_FAILURE;
	}
	// 最初の一行目に列数が記載されている
	fgets(buf,sizeof(buf),fp);
	t = strtol(buf, &tmpptr, 10);
	DPRINT("# of testcases:%ld\n", t);

	// 二行目以降は各テストケース
	for(i = 1; i <= t; i++){
		char *token = NULL, *token2 = NULL;
		unsigned char blue_order[100], orange_order[100];
		unsigned char blue_priority[100], orange_priority[100];
		int b_idx_max = 0, o_idx_max = 0, idx_max = 0;
		memset(buf, 0, sizeof(buf));
		memset(blue_order, 0, sizeof(blue_order));
		memset(orange_order, 0, sizeof(orange_order));
		memset(blue_priority, 0, sizeof(blue_priority));
		memset(orange_priority, 0, sizeof(orange_priority));
		fgets(buf, sizeof(buf), fp);

		// 最初のスペースまではボタンの個数
		token = strtok(buf, " ");
		n = strtol(token, &tmpptr, 10);
		DPRINT("# of buttons:%ld\n", n);

		// 以降はボタンの指示
		while((token = strtok(NULL, " ")) != NULL &&
				(token2 = strtok(NULL, " ")) != NULL){
			DPRINT("token:%s,token2:%s\n",token,token2);
			switch(token[0]){
			case 'B':
				blue_order[b_idx_max] = (char)strtoul(token2, &tmpptr, 10);
				blue_priority[b_idx_max] = idx_max;
				b_idx_max++;
				idx_max++;
				break;
			case 'O':
				orange_order[o_idx_max] = (char)strtoul(token2, &tmpptr, 10);
				orange_priority[o_idx_max] = idx_max;
				o_idx_max++;
				idx_max++;
				break;
			default:
				DPRINT("Internal error\n");
				ret = EXIT_FAILURE;
				goto ERROR;
			}
		}

		// ロボットのアルゴリズムを記述
		int time = 0, priority = 0;
		int blue_pos = 1, orange_pos = 1;
		int b_idx = 0, o_idx = 0;
		bool flag_push = false;
		while(priority < idx_max){
			// 青のロボットの動き
			if(blue_order[b_idx] == 0){
				DPRINT("Blue: Stay at button %d\n", blue_pos);
			}else if(blue_pos == blue_order[b_idx]){
				if(priority == blue_priority[b_idx]){
					DPRINT("Blue: Push button %d\n", blue_pos);
					b_idx++;
					flag_push = true;
				}else{
					DPRINT("Blue: Stay at button %d\n", blue_pos);
				}
			}else if(blue_pos < blue_order[b_idx]){
				blue_pos++;
				DPRINT("Blue: Move to button %d\n", blue_pos);
			}else if (blue_pos > blue_order[b_idx]) {
				blue_pos--;
				DPRINT("Blue: Move to button %d\n", blue_pos);
			}
			// オレンジのロボットの動き
			if(orange_order[o_idx] == 0){
				DPRINT("Orange: Stay at button %d\n", orange_pos);
			}else if(orange_pos == orange_order[o_idx]){
				if(priority == orange_priority[o_idx]){
					DPRINT("Orange: Push button %d\n", orange_pos);
					o_idx++;
					flag_push = true;
				}else{
					DPRINT("Orange: Stay at button %d\n", orange_pos);
				}
			}else if(orange_pos < orange_order[o_idx]){
				orange_pos++;
				DPRINT("Orange: Move to button %d\n", orange_pos);
			}else if (orange_pos > orange_order[o_idx]) {
				orange_pos--;
				DPRINT("Orange: Move to button %d\n", orange_pos);
			}
			time++;
			if(flag_push){
				flag_push = false;
				priority++;
			}
		}
		printf("Case #%d: %d\n", i, time);
	}

ERROR:
	fclose(fp);
	return ret;
}
