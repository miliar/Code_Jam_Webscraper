#include <stdio.h>

int pos[200001];
double vendor[100000];

int main()
{
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int D, C;
		scanf("%d %d", &C, &D);
		int num_vendors = 0;
		int old_num_vendors = 0;
		int gg_num_vendors = 0;
		double temp_pos;
		double end_temp_pos;
		double max_ans = 0.0;
		int gg = 0;
		for (int i = 0; i < C; ++i) {
			int P, V;
			scanf("%d %d", &P, &V);
			temp_pos = P - D * ((double) (V - 1)) / 2;
			gg = 0;
			if (i != 0) {
				if (temp_pos < end_temp_pos) {
					gg = 1;
					temp_pos = end_temp_pos;
				}
			}
			for (int j = 0; j < V; ++j) {
				vendor[num_vendors++] = temp_pos - P;
				temp_pos += D;
			}
			end_temp_pos = temp_pos;
			if (gg == 0) {
				double min = 0, max = 0;
				for (int i = gg_num_vendors; i < old_num_vendors; ++i) {
					if (min > vendor[i])
						min = vendor[i];
					if (max < vendor[i])
						max = vendor[i];
				}
				double ans;
				double df = (max - min);
				ans = df / 2;
				if (ans > max_ans)
					max_ans = ans;
				gg_num_vendors = old_num_vendors;
			}
			old_num_vendors = num_vendors;
		}
		if (1) {
			double min = 0, max = 0;
			for (int i = gg_num_vendors; i < old_num_vendors; ++i) {
				if (min > vendor[i])
					min = vendor[i];
				if (max < vendor[i])
					max = vendor[i];
			}
			double ans;
			double df = (max - min);
			ans = df / 2;
			if (ans > max_ans)
				max_ans = ans;
			gg_num_vendors = old_num_vendors;
		}
		old_num_vendors = num_vendors;
		printf("Case #%d: %f\n", Case, max_ans);
	}
	return 0;
}

