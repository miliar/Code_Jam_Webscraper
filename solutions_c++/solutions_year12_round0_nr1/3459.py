#include <stdio.h>
char map[26] = {
	'y', /* a -> y */
	'h', /* b -> h */
	'e', /* c -> e */
	's', /* d -> s */
	'o', /* e -> o */
	'c', /* f -> c */
	'v', /* g -> v */
	'x', /* h -> x */
	'd', /* i -> d */
	'u', /* j -> u */
	'i', /* k -> i */
	'g', /* l -> g */
	'l', /* m -> l */
	'b', /* n -> b */
	'k', /* o -> k */
	'r', /* p -> r */
	'z', /* q -> z */
	't', /* r -> t */
	'n', /* s -> n */
	'w', /* t -> w */
	'j', /* u -> j */
	'p', /* v -> p */
	'f', /* w -> f */
	'm', /* x -> m */
	'a', /* y -> a */
	'q', /* z -> q */
};
char str[500];
int main()
{
	gets(str);
	int times;
	sscanf(str, "%d", &times);
	for (int c = 1; c <= times; c++)
	{
		gets(str);
		for (int i = 0; str[i]; i++)
		{
			if (str[i] == ' ') continue;
			str[i] = map[str[i] - 'a'];
		}
		printf("Case #%d: %s\n", c, str);
	}

}