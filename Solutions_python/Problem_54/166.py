
def subNOD(a, b):
	if b == 0:
		return a;
	else:
		return subNOD(b, a % b);

def NOD(a, b):
	if a < 0:
		a *= -1;
	if b < 0:
		b *= -1;
	if (a < b):
		c = a;
		a = b;
		b = c;
	return subNOD(a, b);

Input = open('B-large.in', 'r');
Output = open('B-large.out', 'w');


NumberOfTests = int(Input.readline());
for i in range(NumberOfTests):
	s = Input.readline();
	a = s.split(" ");
	nod = int(a[2]) - int (a[1]);
	if nod < 0:
		nod *= -1;
	for j in range(3, int(a[0]) + 1):
		nod = NOD(nod, int(a[j]) - int(a[j - 1]));
	answer = "Case #" + str(i + 1) + ": " + str((nod - (int(a[1]) % nod)) % nod) + "\n";
	Output.write(answer);
	

	
