#include <stdio.h>
#include <assert.h>

char read_char() {
	char c = 'z';
	while (1) {
		scanf("%c", &c);
		switch (c) {
		case '.': case '0': case '1': return c;
		}
	}
	return c;
}

int main() {
	int case_count;
	char results[100][100];
	double wps[100];
	double owps[100];
	scanf("%d", &case_count);
	for (int case_index = 1; case_index <= case_count; ++case_index) {
		int team_count;
		scanf("%d", &team_count);
		for (int i = 0; i < team_count; ++i) {
			for (int j = 0; j < team_count; ++j) {
				results[i][j] = read_char();
			}
		}
		
		for (int i = 0; i < team_count; ++i) {
			double wp = 0.0;
			int count = 0;
			for (int j = 0; j < team_count; ++j) {
				switch (results[i][j]) {
				case '0':
					++count;
					break;
				case '1':
					++count;
					++wp;
					break;
				case '.':
					break;
				default:
					assert(false);
				}
			}
			wps[i] = wp / count;
		}
		for (int k = 0; k < team_count; ++k) {
			double single_owps[100];
			for (int i = 0; i < team_count; ++i) {
				if (results[i][k] != '0' && results[i][k] != '1')
				{
					single_owps[i] = -1;
					continue;
				}
				double owp = 0.0;
				int count = 0;
				for (int j = 0; j < team_count; ++j) {
					if (j == k) continue;
					switch (results[i][j]) {
					case '0':
						++count;
						break;
					case '1':
						++owp;
						++count;
						break;
					case '.':
						break;
					default:
						assert(false);
					}
				}
				single_owps[i] = owp / count;
			}
			owps[k] = 0.0;
			int count = 0;
			for (int i = 0; i < team_count; ++i) {
				if (single_owps[i] == -1) continue;
				owps[k] += single_owps[i];
				++count;
			}
			owps[k] /= count;
		}
		
		printf("Case #%d:\n", case_index);
		for (int i = 0; i < team_count; ++i) {
			double rpi1, rpi2, rpi3;
			rpi1 = wps[i];
			rpi2 = owps[i];
			rpi3 = 0.0;
			int count = 0;
			for (int k = 0; k < team_count; ++k) {
				if (results[i][k] != '0' && results[i][k] != '1')
					continue;
				++count;
				rpi3 += owps[k];
			}
			rpi3 /= count;
			printf("%f\n", 0.25 * rpi1 + 0.5 * rpi2 + 0.25 * rpi3);
		}
	}
}
