#include <cstdio>

int main() {
	int cases;
	scanf("%i", &cases);

	for(int c = 0; c < cases; ++c) {
		int has_combine, has_opposed, char_count, list_pos = 0;
		char combine[4], opposed[3], chars[101], list[100];

		scanf("%i", &has_combine);
		if(has_combine)
			scanf("%s", combine);

		scanf("%i", &has_opposed);
		if(has_opposed)
			scanf("%s", opposed);

		scanf("%i", &char_count);
		scanf("%s", chars);

		for(int i = 0; i < char_count; ++i) {
			if(list_pos == 0) {
				list[list_pos++] = chars[i];
			} else {
				if(has_combine && 
					((combine[0] == chars[i] && combine[1] == list[list_pos - 1]) ||
					(combine[1] == chars[i] && combine[0] == list[list_pos - 1]))) {
						list[list_pos - 1] = combine[2];
				} else {
					bool clear = false;
					if(has_opposed && (chars[i] == opposed[0] || chars[i] == opposed[1])) {
						char look_for = chars[i] == opposed[0] ? opposed[1] : opposed[0];
						for(int n = 0; n < list_pos; ++n) {
							if(list[n] == look_for) {
								clear = true;
								break;
							}
						}
					}
					
					if(clear)
						list_pos = 0;
					else
						list[list_pos++] = chars[i];
				}
			}
		}
		
		printf("Case #%i: [", c + 1);
		for(int i = 0; i < list_pos; ++i) {
			printf("%c", list[i]);
			if(i != list_pos - 1)
				printf(", ");
		}
		printf("]\n");
	}

	return 0;
}