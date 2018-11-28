#include <stdio.h>
#include <string>
#include <map>
#include <set>

struct dtree
{
	double weight;
	int feat;
	dtree *left, *right;

	~dtree()
	{
		delete left;
		delete right;
	}
};

std::map<std::string, int> feats;
int next_feat;

dtree* read_dtree()
{
	static char name[11];
	static double weight;
	int feat;
	switch (scanf(" (%lf %[a-z]", &weight, name))
	{
		case 0: return NULL;
		case 1: feat = 0;
		case 2:
		{
			int &feat_ref = feats[name];
			if (feat_ref == 0)
				feat_ref = next_feat++;
			feat = feat_ref;
		}
	}
	//puts("read");
	dtree *dt = new dtree;
	dt->weight = weight;
	dt->feat = feat;
	dt->left = read_dtree();
	dt->right = read_dtree();
	scanf(" ) ");
	return dt;
}

std::set<int> fs;
double pr;

void cute(dtree *dt)
{
	if (!dt)
		return;
	pr *= dt->weight;
	if (fs.find(dt->feat) != fs.end())
		cute(dt->left);
	else
		cute(dt->right);
}

int main()
{
	int tc;
	scanf("%d\n", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d", &next_feat);
		feats.clear();
		next_feat = 1;
		dtree *dt = read_dtree();

		char name[11], buff[11];
		int n, k;
		scanf("%d", &n);
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; i++)
		{
			fs.clear();
			scanf("%s %d", name, &k);
			while (k--)
			{
				scanf("%s", buff);
				int &feat = feats[buff];
				if (feat == 0)
					feat = next_feat++;
				fs.insert(feat);
			}
			pr = 1.0;
			cute(dt);
			printf("%.7f\n", pr);
		}

		delete dt;
	}
	return 0;
}