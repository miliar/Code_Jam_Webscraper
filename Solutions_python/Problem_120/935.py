def count_line(paint_data):
	paintamt = paint_data[1]
	whiteradius = paint_data[0]
	p = paintamt
	c = 0
	r = whiteradius
	paint = 0
	x = 1
	while (x!=0):
		paint = paint + (((r+1)**2) - (r**2))
		if (paint <= paintamt):
			c = c+1
			r = r+2
		else:
			break

	return c



def readfile():
	output = []
	with open("A-small-attempt0.in","r") as f:
		trials = f.readline()
		print trials
		for i in range(int(trials.strip())):
			paint_data = map(int, f.readline().split())
			outline = "Case #%d: %s" % (i+1, str(count_line(paint_data)))
			print outline
			output.append(outline)

	with open("paint_small_output.out","w") as f:
		f.write("\n".join(output))


if __name__=="__main__":
	readfile()