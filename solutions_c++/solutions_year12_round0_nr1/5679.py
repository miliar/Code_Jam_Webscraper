#include <stdio.h>
#include <string.h>

static const size_t BUFF_SIZE = 128;

//                                  abcdefghijklmnopqrstuvwxyz
static const char * const DECODE = "yhesocvxduiglbkrztnwjpfmaq";

int N = 0;

void solve(const char * const in, char *out) {
	size_t len = strlen(in);
	for (size_t i = 0; i < len; ++i) {
		if (' ' == in[i] || '\n' == in[i]) {
			out[i] = in[i];
		} else {
			out[i] = DECODE[in[i] - 'a'];
		}
	}
}

int main() {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	scanf("%d\n", &N);

	for (int i = 0; i < N; ++i) {
		char inp[BUFF_SIZE] = {0, };
		char out[BUFF_SIZE] = {0, };
		fgets(inp, BUFF_SIZE, stdin);
		solve(inp, out);
		printf("Case #%d: %s", i + 1, out);
	}

	return 0;
}
