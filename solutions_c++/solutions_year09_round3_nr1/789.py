// happy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <string.h>

#include   <math.h>   


#define IN_FILE_NAME "in.txt"
#define OUT_FILE_NAME "out.txt"

unsigned __int64 execute_base_number(char *begin, char *end)
{
	int hash[128] = {0};
	int seq[128];
	int i = 0, base = 0;
	char *data = begin;
	unsigned __int64 number = 0;
	unsigned __int64 power = 1;
	
	for (i = 0; i < 128; i++) {
		seq[i] = -1;
	}

	for (data = begin; data != end; data++) {
		if (*data >= 'a' && *data <= 'z') {
			hash[*data] = 1;
		} else if (*data >= '0' && *data <= '9') {
			hash[*data] = 1;
		} else {
			goto err;
		}
	}

	for (i = 0, base = 0; i < 128; i++) {
		if (hash[i] == 1) {
			base++;
		}
	}

	if (1 == base) {
		base = 2;
	}

	for (data = begin, i = 0; data != end; data++) {
		if (0 == i) {
			seq[*data] = 1;
			i++;
		} else if (1 == i) {
			if (seq[*data] == -1) {
				seq[*data] = 0;
				i++;
			}
		} else {
			if (seq[*data] == -1) {
				seq[*data] = i;
				i++;
			}			
		}
	}

	for (data = end - 1; data != begin - 1; data--) {
		number += seq[*data] * power;
		power = power * base;
	}

err:
	return number;
}

int main(int argc, char* argv[])
{
	FILE *in_fp = NULL;
	FILE *out_fp = NULL;
	char line[1000000];
	int n = 0;
	int i = 0, j = 0;
	int count = 0;
	unsigned __int64 number;
	
	
	in_fp = fopen(IN_FILE_NAME, "r");
	
	if (!in_fp) {
		goto err;
	}
	
	out_fp = fopen(OUT_FILE_NAME, "w");
	if (!out_fp) {
		goto err;
	}
	
	if (fgets(line, sizeof(line), in_fp)) {
		sscanf(line, "%d", &n);
	} else {
		goto err;
	}
	
	if (n < 1 || n > 100) {
		goto err;
	}
	
	for (i = 0; i < n; i++) {
		if (fgets(line, sizeof(line), in_fp)) {
			if (line[strlen(line) - 1] == '\n') {
				line[strlen(line) - 1] = '\0';
			}
			if (strlen(line) > 61 || strlen(line) < 1) {
				goto err;
			}
			number = execute_base_number(line, line + strlen(line));
			fprintf(out_fp, "Case #%d: %I64u\n", i + 1, number);
		} else {
			goto err;
		}
	}
	
err:
	if (in_fp) {
		fclose(in_fp);
		in_fp = NULL;
	}
	
	if (out_fp) {
		fclose(out_fp);
		out_fp = NULL;
	}
	
	return 0;
}

