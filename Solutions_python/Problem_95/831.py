
sourceFile = "small.in";
outputFile = "small.out";

s_handler = open(sourceFile, 'r');
o_handler = open(outputFile, 'w');

T = s_handler.readline();

maps = [];

for i in range(0, 26):
	maps.append(0);

ori = [];
ori.append("ejp mysljylc kd kxveddknmc re jsicpdrysi");
ori.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
ori.append("de kr kd eoya kw aej tysr re ujdr lkgc jv");

des = [];

des.append("our language is impossible to understand");
des.append("there are twenty six factorial possibilities");
des.append("so it is okay if you want to just give up");

maps[25] = ord('q');
maps[16] = ord('z');

for i in range(0, len(ori)):
	for j in range(0, len(ori[i])):
		if (ori[i][j] == ' '):
			continue;
		ind = ord(ori[i][j]) - ord('a');
		maps[ind] = ord(des[i][j]);


for i in range(1, int(T)+1):
	result = "";
	line = s_handler.readline().strip();
	for j in range(0, len(line)):
		if (line[j] == ' '):
			result += line[j];
		else:
			result += chr(maps[ord(line[j]) - ord('a')]);
	o_handler.write("Case #" + str(i) + ": " + result + "\n");

s_handler.close();
o_handler.close();
